__author__ = 'pointschan'



class Thing(object):
    def test(self, str):
        print str



#Class instantiation uses function notation -
#creates a new instance of the class and assigns this object to the local variable a
a = Thing()

#A method can be called right after it is bound
a.test("hello")


class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

b = MyClass()
print b.i
print b.f()