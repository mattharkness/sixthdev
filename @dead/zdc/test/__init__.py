
import unittest
from sqlTest import dbc

from testIdxDict import *
from testRecord import *
from testObject import *
from testRecordObject import *
from testTable import *
from testLinkSet import *

suites = {
    "LinkSet": unittest.makeSuite(LinkSetTestCase, "check_"),
    "IdxDict": unittest.makeSuite(IdxDictTestCase, "check_"),
    "Record": unittest.makeSuite(RecordTestCase, "check_"),
    "Object": unittest.makeSuite(ObjectTestCase, "check_"),
    "RecordObject" : unittest.makeSuite(RecordObjectTestCase, "check_"),
    "Table": unittest.makeSuite(TableTestCase, "check_"),
    }

import zikebase.test
import zikeshop.test
suites.update(zikebase.test.suites)
suites.update(zikeshop.test.suites)


#@TODO: why not have some sort of scheme where if suite=="ALL"
#@TODO: it just magically loops through all the tests in __all__ ?
#@TODO: and applies makeSuite for "check_"...?
