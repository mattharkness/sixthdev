
### rantelope object model ####################################
__ver__="$Id"

from strongbox import *
import crypt

# NOTE: all ID attributes must default
# to "None" for SQLite's autonumbering
# this doesn't effect MySQL's auto_increment 
auto = None


class Author(Strongbox):
    ID = attr(long, default=auto)
    fname = attr(str)
    lname = attr(str)
    email = attr(str)
    homepage = attr(str)
    username = attr(str)
    cryptpwd = attr(str)
    
    def set_password(self, value):
        #@TODO: randomize the crypt salt
        self.cryptpwd = crypt.crypt(value, "xx")
    def get_password(self, value):
        raise ValueError, "passwords are encrypted"
    def isPassword(self, value):
        return self.cryptpwd == crypt.crypt(value, self.cryptpwd[:2])


class Comment(Strongbox):
    """
    A comment posted by a reader.
    """
    ID = attr(long, default=auto)
    storyID = attr(long)
    name = attr(str)
    mail = attr(str)
    url = attr(str)
    note = attr(str)

class Story(Strongbox):
    """
    A document, blog entry, or other text.
    """
    ID = attr(long, default=auto)
    channelID = attr(long)
    categoryID = attr(long, default=0)
    title = attr(str)
    url = attr(str)
    description = attr(str)
    comments = linkset(Comment)
    author = link(Author)

class Category(Strongbox):
    """
    A category of story.
    """
    ID = attr(long, default=auto)
    channelID = attr(long)
    name = attr(str)


## xml stuff for Channel.
## @TODO: xml/xslt stuff should get its own file (??)
try:
    plainXSLT = open("plain.xsl").read()
except:
    raise Warning, "what happened to plain.xsl?!?!?!"

def transform(xml, xsl):
    """
    A simple wrapper for 4XSLT.
    """
    from Ft.Xml.Xslt.Processor import Processor
    from Ft.Xml.InputSource import DefaultFactory
    proc = Processor()
    xslObj = DefaultFactory.fromString(xsl, "http://rantelope.com/")
    proc.appendStylesheet(xslObj)
    xmlObj = DefaultFactory.fromString(xml)
    return proc.run(xmlObj)



class Channel(Strongbox):
    """
    A collection of Stories. (A blog, for example)
    """
    ID = attr(long, default=auto)
    title = attr(str)
    url = attr(str)
    description = attr(str)
    rssfile = attr(str, okay="([^/]+.rss|^$)" )
    htmlfile = attr(str, okay="([^/]+|^$)" )
    template = attr(str, default=plainXSLT)
    stories = linkset(Story)
    categories = linkset(Category)
    path = attr(str, default="./out/")

    def toRSS(self):
        import zebra
        return zebra.fetch("rss", BoxView(self))

    def toHTML(self, input=None):
        RSS = input or self.toRSS()
        res = transform(RSS, self.template)
        res = "\n".join(res.split("\n")[1:])
        return res

    def writeFiles(self):
        """
        temporarily disabled: use blog.app instead
        """
        rss = self.toRSS()
        if self.rssfile:
            print >> open(self.path + self.rssfile, "w"), rss
        if self.htmlfile and self.template:
            print >> open(self.path + self.htmlfile, "w"), self.toHTML(rss)
