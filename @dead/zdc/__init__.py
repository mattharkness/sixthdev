"""
zdc: zike data classes (wrapper for python db-api 2.0)
"""
__ver__="$Id$"

# the two basic classes:
from IdxDict import IdxDict
from Object import Object

# these build on the above:
from Field import Field
from Table import Table
from Record import Record
from RecordObject import RecordObject
from ObjectView import ObjectView
from LinkSet import LinkSet
from Junction import Junction
from FixedPoint import FixedPoint
from Connection import Connection


    
# @TODO: we need to know which module 'dbc' comes from, because
# we need to get certain constants (eg, for field types)
# that are in the module, but not connected to the
# connection object... This is a shortcoming of the DB-API.. :/
from MySQLdb import NUMBER, TIMESTAMP

###############

def sqlEscape(s):
    #@TODO: get the real version of this out of Record
    import string
    return string.replace(s, "'", "\\'")


def sqlSet(*data):
    """returns a string with a SQL set containing whatever you pass in"""
    set = []
    for item in data:
        
        # we don't accept dicts.
        if type(item) == type({}):
            raise TypeError, "sqlSet we can't handle dicts"

        # but we DO accept lists and tuples
        elif type(item) in (type(()), type([])):
            set = set+list(item)

        # ... as well as scalars.
        else:
            set.append(item)

    # stringify the set
    res = str(tuple(set))

    # one-item tuples have a "," at the end, but
    # sql doesn't like that.
    if res[-2]==",":
        res = res[:-2]+")"
        
    return res


def toListDict(cur):
    """converts cursor.fetchall() results into a list of dicts"""
    res = []
    for row in cur.fetchall():
        dict = {}
        for i in range(len(cur.description)):
            dict[cur.description[i][0]] = row[i]
        res.append(dict)
    return res



def find(what, where=None, orderBy=None, _select=None):
    """
    find(what, where, orderBy) -> list of what's matching where
    what is a zdc.RecordObject class
    where is a SQL where clause
    orderBy is a SQL order by clause

    this is how to do ad-hoc SQL queries for objects..
    """
    #@TODO: test case for this.. (it was factored out of zikeshop)
    if _select:
        # this is a really dumb kludge at the moment..
        sql = _select
    else:
        tablename = what._table.name
        sql = "SELECT ID FROM %s " % tablename
    if where:
        sql = sql + " WHERE %s " % where
    if orderBy:
        sql = sql + " ORDER BY %s " % orderBy
    cur = what._table.driver.dbc.cursor()
    cur.execute(sql)
    res = []
    for row in cur.fetchall():
        res.append(what(ID=row[0]))
    return res
