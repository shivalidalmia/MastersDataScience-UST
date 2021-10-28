#
#  L9-5.1: sum_multiples_1.py (no submission required)
#
# Problem: add up even multiples of 3 or 5, from 1..9
#
# First, we do it the imperative state-changing way: NOT FUNCTIONAL
#

s = 0 # this accumulator object changes state...

for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        s += n
        
print(s)

