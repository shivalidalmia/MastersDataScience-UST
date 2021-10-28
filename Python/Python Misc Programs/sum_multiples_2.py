#
#  L9-5.2: sum_multiples_2.py (no submission required)
#
#
# Next: the object-oriented way with a list
#

m = list() # this accumulator object changes state...

for n in range(1, 10):
    if n % 3 == 0 or n % 5 == 0:
        m.append(n)

print(sum(m))

