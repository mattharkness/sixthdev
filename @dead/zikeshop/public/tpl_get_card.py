class Report:

    def show(self, model={}):
        print self.fetch(model)

    def fetch(self, model={}):
        import copy   # used by scope
        self.model = model
        scope = model
        scope_stack = []
        zres = ""
        import tpl_head
        zres = zres+ tpl_head.fetch(scope)
        zres = zres + '<'
        zres = zres + 'h1'
        zres = zres + '>'
        zres = zres + 'Credit Card'
        zres = zres + '<'
        zres = zres + '/h1'
        zres = zres + '>'
        if scope.get('error',''):
            zres = zres + '<'
            zres = zres + 'h2'
            zres = zres + '>'
            zres = zres + '<'
            zres = zres + 'font color=\"red\"'
            zres = zres + '>'
            zres = zres + str(scope.get('error',''))
            zres = zres + '<'
            zres = zres + '/font'
            zres = zres + '>'
            zres = zres + '<'
            zres = zres + '/h2'
            zres = zres + '>'
        _ = 0
        _max_ = len(self.model["creditcards"])
        scope_stack.append(scope)
        scope = copy.copy(scope)
        scope.update(locals())
        for _ in range(_max_):
            scope.update(self.model["creditcards"][_])
            scope["_"] = _
            if _ == 0:
                zres = zres + '<'
                zres = zres + 'form action=\"checkout.py\" method=\"POST\"'
                zres = zres + '>'
                zres = zres + '<'
                zres = zres + 'h3'
                zres = zres + '>'
                zres = zres + 'Select a credit card from the list below...'
                zres = zres + '<'
                zres = zres + '/h3'
                zres = zres + '>'
                zres = zres + '<'
                zres = zres + 'select name=\"cardID\"'
                zres = zres + '>'
            zres = zres + '<'
            zres = zres + 'option value=\"'
            zres = zres + str(scope.get('ID',''))
            zres = zres + '\"'
            zres = zres + '>'
            zres = zres + str(scope.get('maskedNumber',''))
            zres = zres + '<'
            zres = zres + '/option'
            zres = zres + '>'
            if _ + 1 == _max_:
                zres = zres + '<'
                zres = zres + '/select'
                zres = zres + '>'
                zres = zres + '<'
                zres = zres + 'input type=\"hidden\" name=\"action\" value=\"update\"'
                zres = zres + '>'
                zres = zres + '<'
                zres = zres + 'input type=\"submit\" value=\"submit\"'
                zres = zres + '>'
                zres = zres + '<'
                zres = zres + '/form'
                zres = zres + '>'
            zres = zres + '<'
            zres = zres + 'h3'
            zres = zres + '>'
            zres = zres + '... or enter a new card below:'
            zres = zres + '<'
            zres = zres + '/h3'
            zres = zres + '>'
        scope = scope_stack.pop()
        del _
        if not _max_:
            zres = zres + '<'
            zres = zres + 'h3'
            zres = zres + '>'
            zres = zres + 'enter your credit card info below:'
            zres = zres + '<'
            zres = zres + '/h3'
            zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'form action=\"checkout.py\" method=\"post\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'b'
        zres = zres + '>'
        zres = zres + 'name on card:'
        zres = zres + '<'
        zres = zres + '/b'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"text\" name=\"name\" value=\"\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'br'
        zres = zres + '>'
        zres = zres + '\ncard number: '
        zres = zres + '<'
        zres = zres + 'input type=\"text\" name=\"number\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'br'
        zres = zres + '>'
        zres = zres + '\n\nexpiration month:'
        zres = zres + '<'
        zres = zres + 'select name=\"expMonth\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '01'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '02'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '03'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '04'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '05'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '06'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '07'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '08'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '09'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '10'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '11'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '12'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/select'
        zres = zres + '>'
        zres = zres + '\n\nyear:'
        zres = zres + '<'
        zres = zres + 'select name=\"expYear\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2000'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2001'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2002'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2003'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2004'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2005'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2006'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'option'
        zres = zres + '>'
        zres = zres + '2007'
        zres = zres + '<'
        zres = zres + '/option'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/select'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'br'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"hidden\" name=\"context\" value=\"checkout\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"hidden\" name=\"action\" value=\"addcard\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + 'input type=\"submit\" value=\"submit\"'
        zres = zres + '>'
        zres = zres + '<'
        zres = zres + '/form'
        zres = zres + '>'
        import tpl_foot
        zres = zres+ tpl_foot.fetch(scope)
# end of Report.fetch()
        return zres

def fetch(model={}):
    return Report().fetch(model)
    
def show(model={}):
    return Report().show(model)
