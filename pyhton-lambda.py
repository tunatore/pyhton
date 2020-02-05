'''
Created on Jul 31, 2013

@author: tuna
'''


# lambdas are similar to functions in python with simple syntax
# do define a increment lambda
# first function example below
def addNumbers(x, y):
    return x + y


print(addNumbers(2, 2))

# output 4
# same thing with short lambda syntax

l = lambda x, y: x + y

print("lambda output ", l(2, 2))
# lambda output 4

# another example return abs value
l = lambda x: abs(x)

print("lambda abs output", l(-1999))
# lambda abs output 1999
print("lambda abs output", l(6))
# lambda abs output 6

# filtering list using lambda

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# filtering numbers greater then 10
print(list(filter(lambda x: x > 0, numberList)))
# output [11, 12, 13, 14, 15]

# showing only even numbers
print(list(filter(lambda x: x % 2 == 0, numberList)))
# output [2, 4, 6, 8, 10, 12, 14]

# lambda different syntax
print((lambda x: abs(x))(-100))
# 100

# lambda different syntax
print((lambda x, y, z: x * y * z)(3, 4, 5))
# output 60

nameList = ["Tornado", "Tuna", "Bob"]
for name in nameList:
    print((lambda x: x.startswith('T'))(name))
# True
# True
# False
