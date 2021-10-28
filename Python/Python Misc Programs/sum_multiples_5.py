#
#  L9-5.5: sum_multiples_5.py (no submission required)
#

# Python treats functions as first-class objects:
#
# First-class objects are:
#   • Created at runtime
#   • Assigned to a variable or element in a data structure
#   • Passed as an argument to a function
#   • Returned as the result of a function
#

# a new example: computing n! = n*(n-1)*...*3*2*1

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

print (factorial(47))
print (factorial.__doc__)
print (type(factorial))

# use function through different name, passing as argument to map

fact = factorial

print (list(map(fact,range(11)))) # map applies fact to each element of range(11)

