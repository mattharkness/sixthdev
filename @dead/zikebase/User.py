"""
User.py - user object for zikebase

$Id$
"""

import zikebase
zikebase.load("Password")
zikebase.load("Contact")
import zdc

#@TODO: refactor all this nonsense into MultiTableRecordObject!
class User(zikebase.Contact):
    __super = zikebase.Contact
    passwordClass = zikebase.Password
    _links = {
        #@TODO: this doesn't seem to be working..
        "contacts": [zdc.LinkSet, zikebase.Contact, "userID"],
        }
        
    def _new(self):
        self.__super._new(self)
        self._userRec = zdc.Table(zikebase.dbc, "base_user").new()

    def getEditableAttrs(self):
        return self.__super.getEditableAttrs(self) \
               + ['username', 'password', 'uid', 'siteID']
        
    def _fetch(self, key=None, **kw):
        keys = kw.keys()
        if len(keys) > 1:
            # multi-colum might actually work, but I wouldn't bet on it, so
            # I'm preventing it for now...
            raise Error, \
                  "User._fetch can't cope with multiple columns yet."

        elif (len(keys)==1) and (keys[0] in ['username', 'password']):
            # search by the detail record..
            table = zdc.Table(zikebase.dbc, "base_user")
            self._userRec = table.fetch(key)
            apply(self.__super._fetch, (self,), {"ID":self._userRec["ID"]})

        else:
            # search by the master record..
            apply(self.__super._fetch, (self,), kw)
            self._userRec = zdc.Table(zikebase.dbc, "base_user").fetch(self.ID)


    def set_uid(self, value):
        self._userRec['uid'] = value
    def get_uid(self):
        return self._userRec['uid']
    
    def set_username(self, value):
        self._userRec['username'] = value
    def get_username(self):
        return self._userRec['username']

    def set_siteID(self, value):
        self._userRec['siteID'] = value
    def get_siteID(self):
        return self._userRec['siteID']
        
    # we want to encrypt the passwords transparently.
    def get_password(self):
        """
        returns a zikebase.Password object for testing against plaintext.
        """
        return self.passwordClass(self._userRec["password"])
    
    def set_password(self, value):
        """
        user.password = 'whatever'  # Transparently encrypt the password
        """
        pw = self.passwordClass()
        pw.set(value)
        self._userRec["password"] = pw.crypted
        
    def save(self):
        self.__super.save(self)
        self._userRec["ID"]=self.ID
        if not self.uid:
            import weblib
            self.uid = weblib.uid()
        if not self.username:
            self.username = ""
        self._userRec.save()
