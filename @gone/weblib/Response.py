"""
Response.py - loosely emulates the ASP Response object for python CGI's
"""
__ver__="$Id$"

import weblib
import string
import sys
import os

class Response(object):
    """
    Response object similar to the one from ASP
    """

    ## attributes ########################################

    contentType = "text/html"
    headers = []
    cookies = []
    buffer = ""
    _sentHeaders = 0
       

    ## constructor #######################################

    def __init__(self, engine=None, out=None):

        self.engine = engine
        self.out = out
       

    #### I/O Methods (needed for print redirection) ########

    def softspace(self):
        pass


    def flush(self):
        if self.out:
            if not self._sentHeaders:
                self.out.write(self.getHeaders())
                self._sentHeaders = 1
                
            self.out.write(self.buffer)
            self.buffer = ""
    

    #### PUBLIC METHODS ####################

    def start(self):
        """start() ... from the Part interface.."""
        self.clear()
        

    def write(self, data):
        self.buffer = self.buffer + data


    def getHeaders(self):
        res = "Content-type: " + self.contentType + "\n"
        for h in self.headers:
            # each header is a (key, value) tuple
            if h[1] is not None:
                res = res + h[0] + ": " + h[1] + "\n"
            #@TODO: should h[1]==None throw an error?
        return res + "\n"


    def addHeader(self, key, value):
        self.headers = self.headers + [(key, value)]


    # @TODO: actually populate the cookies list
    def addCookie(self, key, value):
        self.addHeader("Set-Cookie", key + "=" + value)


    def end(self):
        self.flush()
        sys.exit()


    def redirect(self, url):
        # http://ppewww.ph.gla.ac.uk/~flavell/www/post-redirect.html
        # except it doesn't work with IIS, so:
        server = os.environ.get('SERVER_SOFTWARE', '')
        if string.find(server, 'Microsoft')<>-1:
            self.clear()
            self.write(weblib.trim(
                '''
                <SCRIPT language="Javascript">
                document.location='%s';
                </SCRIPT>
                ''' % url))
            self.end()
        self.addHeader("Status", "303")
        self.addHeader("Location", url)
        self.end()


    def clear(self):
        """Reset all attributes to their defaults.."""

        for atr in ('contentType', 'headers', 'cookies', 'buffer'):
            setattr(self, atr, getattr(self.__class__, atr))

        self._sentHeaders = 0
            

    #### NOT IMPLEMENTED YET #####################
    #
    # these are part of the ASP Response object
    # but not this one:
    #
    # appendToLog() - doesn't really apply to apache
    # binaryWrite() - do we need this?
    # flush() - also for buffering.. could do someday
    #
    # cacheControl - the cache-control header
    # charSet - the charset header
    # contentType - the content-type header
    # expires - the expires header, in... minutes?
    # expiresAbsolute - the expires header as a date
    # isClientConnected - browser still connected?
    # PICS - a PICS content-rating label
    # Status - HTTP response code.. can i change this?!?
    #
    # Cookies - replaced by addCookie()

