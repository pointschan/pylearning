__author__ = 'pointschan'

def cheeseshop(kind, *arguments, **keywords):

    print "kind = " + kind
    print "-" * 40
    print "arguments = "
    print arguments
    for arg in arguments:
        print arg
    print "-" * 40
    print "keywords = "
    print keywords
    keys = keywords.keys()
    for kw in keys:
        print kw, ":", keywords[kw]



cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper='Michael Palin',
           client="John Cleese",
           sketch="Cheese Shop Sketch")
