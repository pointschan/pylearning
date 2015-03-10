__author__ = 'pointschan'

"""
Generally speaking, instance variables are for data unique to each instance and
class variables are for attributes and methods shared by all instances of the class.

Shared data can have possibly surprising effects with involving mutable objects
such as lists and dictionaries. For example, the tricks list in the following code
should not be used as a class variable because just a single list would be shared
by all Dog instances
"""

class Dog_publictricks:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


class Dog_privatetricks:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


f = Dog_publictricks("Fido")
b = Dog_publictricks("Buddy")

f.add_trick("roll over")
b.add_trick("play dead")

print f.name, f.tricks
print b.name, b.tricks


d = Dog_privatetricks("Fido_2")
e = Dog_privatetricks("Buddy_2")


d.add_trick("roll over")
e.add_trick("play dead")

print d.name, d.tricks
print e.name, e.tricks