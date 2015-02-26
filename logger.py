__author__ = 'Charles'

def logger(func):
    print 'logger'
    def inner(*args, **kwargs): #1
        print ('Entering (inner)', func.__name__)
        print "Arguments were: %s, %s" % (args, kwargs)
        print 'before inner return'
        return func(*args, **kwargs) #2
    print 'after inner return'
    return inner

@logger
def foo1(x, y=1):
    print 'enter foo1'
    return x * y

@logger
def foo2():
    return 2

f1 = foo1(8)
print f1

f2 = foo2()
print f2