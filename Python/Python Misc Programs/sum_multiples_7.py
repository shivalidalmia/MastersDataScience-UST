#
#  L9-5.7: sum_multiples_7.py (no submission required)
#

# List comprehensions build lists from sequences or other iterable types
#   by filtering and transforming

# Most functional languages have functions filter() and map() which can be composed to
#   achieve the same effect

# Example with map() and filter()

symbols = '0123456789'

codes = list(map(ord,filter(lambda c: ord(c)%2==0, symbols))) # , map(ord,symbols)))
print (codes)
# not so clear, is it?
