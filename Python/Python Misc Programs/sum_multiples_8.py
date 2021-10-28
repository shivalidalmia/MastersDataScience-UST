#
#  L9-5.8: sum_multiples_8.py (no submission required)
#
# Finally: do original 'sum multiples of 3 or 5...' problem using map and filter

codes = sum(filter(lambda x: x%3==0 or x%5==0, map(lambda x: x,range(1,10))))
print (codes)

import functools
import operator

# Can also do this using functools.reduce and operator.add:
# Python's sum is shortcut for reduce(+,some_list)

codes = functools.reduce(operator.add,filter(lambda x: x%3==0 or x%5==0, map(lambda x: x,range(1,10))))
print (codes)
