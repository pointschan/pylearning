__author__ = 'pointschan'

from collections import OrderedDict
from odbchelper import *
import unittest


class testBuildConnectionStringFunctions(unittest.TestCase):

    def setUp(self):
        self.params = OrderedDict([("server","mpilgrim"),
                ("database","master"),
                ("uid","sa"),
                ("pwd","secret")
                ])
        self.paramsx = {"server":"mpilgrim",
                    "database":"master",
                    "uid":"sa",
                    "pwd":"secret"
                    }

    def testBuildConnectionString(self):
        """Build a connection string from a dictionaryof parameters.

        Returns string."""
        print self.params
        dbConnectionString = buildConnectionString(self.params)
        self.assertEqual(dbConnectionString, "server=mpilgrim;database=master;uid=sa;pwd=secret")


    def testBuildConnectionStringx(self):
        print self.paramsx
        dbConnectionStringx = buildConnectionString(self.paramsx)
        print dbConnectionStringx
        self.assertEqual(dbConnectionStringx, "server=mpilgrim;database=master;uid=sa;pwd=secret")

print __name__
if __name__ == "__main__":
    unittest.main()

