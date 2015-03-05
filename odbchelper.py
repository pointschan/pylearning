__author__ = 'Charles'

from collections import OrderedDict

def buildConnectionString(params):
        """Build a connection string from a dictionary of parameters.

        Returns string."""
        print params
        return ";".join(["%s=%s" % (a, b) for a, b in params.items()])

def buildConnectionStringx(**paramx):
        """Build a connection string from a dictionary of parameters.
        Returns string."""
        return ";".join(["%s=%s" % (k, v) for k, v in paramx.items()])

print __name__
if __name__ == "__main__":
        myParams = OrderedDict([("server","mpilgrim"), \
                    ("database","master"), \
                    ("uid","sa"), \
                    ("pwd","secret") \
                    ])
        print buildConnectionString(myParams)

        myParams2 = {"pwd":"secret", \
                    "uid":"sa", \
                    "database":"master", \
                    "server":"mpilgrim" \
                    }
        print buildConnectionString(myParams2)




print buildConnectionStringx(server="xmpilgrim",database="xmaster",uid="xsa",pwd="xsecret")