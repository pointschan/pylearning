__author__ = 'pointschan'


#to create a list of squares
squares = []
for x in range(10):
    squares.append(x**2)
print squares

#create the same list of squares as above
squares =  [x**2 for x in range(10)]
print squares

#can also use built-in function map() and lambda expression
#map(function, sequence)
squares = map(lambda x: x**2, range(10))
print squares

# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses. The result will be a new list resulting from evaluating
# the expression in the context of the for and if clauses which follow it. For example, this
# listcomp combines the elements of two lists if they are not equal:
li =  [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print li