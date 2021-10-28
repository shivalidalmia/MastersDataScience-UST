#
#  L9-5: sum_multiples_raw.py
#

# each of the sum_multiple_N.py examples, in succession...
#    (no submission required)

#
# the imperative state-changing way
#

s = 0 # this accumulator object changes state...
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        s += n
print(s)

#
# the object-oriented way with a list
#

m = list() # this list object changes state...
for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)
print(sum(m))

# #
# # subclass of list which has its own sum
# # (sum() as function is equivalent to sum() as method
# #
#
# class Summable_List(list):
#     def sum(self):
#         s = 0
#         for v in self:
#             s += v
#         return s

# defining sum recursively for lists: look, no state!
#   (but no filtering - yet)

def sumr(seq):
    if len(seq) == 0:
        return 0
    return seq[0] + sumr(seq[1:])

print (sumr([k for k in range(1,10)]))

# defining sequence of values recursively:
# note use of passed function filter_func
# functional programming makes functions first-class data

def until(n, filter_func, v):
    if v == n:
        return []
    if filter_func(v):
        return [v] + until(n, filter_func, v+1)
    else:
        return until(n, filter_func, v+1)

mult_3_5 = lambda n: n%3==0 or n%5==0

print(until (10, mult_3_5, 0))
print(until (10, lambda n: n%3==0 or n%5==0, 0))
print(sumr(until (10, lambda n: n%3==0 or n%5==0, 0)))

# mostly functional version

print(sum(n*n for n in range(1, 10) if n%3==0 or n%5==0))
#  range(n) is a generator expression: it yields a sequence
#   of values 0,1,...,n-1 and is iterable

# now to iteratively compute math.sqrt(2)

def next_(n, x):
    return (x+n/x)/2

f = lambda x: next_(2,x)

print ([round(x,4) for x in (1.0, f(1.0), f(f(1.0)), f(f(f(1.0))))])

def repeat(f, a):
    yield a
    for v in repeat(f, f(a)):
        yield v

print (repeat,2)

# treating function as object
# first-class objects are:
# Created at runtime
# • Assigned to a variable or element in a data structure
# • Passed as an argument to a function
# • Returned as the result of a function

def factorial(n):
    '''returns n!'''
    return 1 if n < 2 else n * factorial(n-1)

print (factorial(47))
print (factorial.__doc__)
print (type(factorial))

# use function through different name, passing as argument

fact = factorial

print (list(map(fact,range(11)))) # applies fact to each element of range(11)

# higher-order functions take function as arg and/or return function as result

# list comprehensions and generator expressions

# A quick way to build a sequence is using a list comprehension (if the target is a list)
# or a generator expression (for all other kinds of sequences).
#

symbols = '0123456789'
codes = []
for symbol in symbols:
    if ord(symbol)%2==0:
        codes.append(ord(symbol))
print (codes)

# list comprehension (lc) of above: all names are local
symbols = '0123456789'
codes = [ord(symbol) for symbol in symbols if ord(symbol)%2 == 0]
print (codes)
print (list(ord(symbol) for symbol in symbols if ord(symbol)%2 == 0))

# lc's build lists from sequences or other iterable types by filtering and transforming

# most functional languages have functions filter() and map() which can be composed to
#   achieve the same effect

codes = list(map(ord,filter(lambda c: ord(c)%2==0, symbols))) # , map(ord,symbols)))
print (codes)

# finally: do original problem using map and filter

codes = sum(filter(lambda x: x%3==0 or x%5==0, map(lambda x: x,range(1,10))))
print (codes)

import functools
import operator

# can also do this using functools.reduce and operator.add: sum is shortcut for reduce

codes = functools.reduce(operator.add,filter(lambda x: x%3==0 or x%5==0, map(lambda x: x,range(1,10))))
print (codes)
