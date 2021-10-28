#
#  L9-5.4: sum_multiples_4.py (no submission required)
#

# mostly functional version using generator sequence as sum() arg

print(sum(n for n in range(1, 10) if n%3==0 or n%5==0))

# arg to sum is a generator expression...

#  range(n) is also a generator expression: it yields a sequence
#   of values 0,1,...,n-1 and is iterable

