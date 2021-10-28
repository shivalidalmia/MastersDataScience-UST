#
#  L9-5.6: sum_multiples_6.py (no submission required)
#

# Higher-order functions take function as arg and/or return function as result

# A quick way to build a sequence is using a list comprehension (if the target is a list)
# or a generator expression (for all other kinds of sequences).
#

# new problem: print out even-ascii-numbered single digit chars

symbols = '0123456789'
codes = []
for symbol in symbols:
    if ord(symbol)%2==0:
        codes.append(ord(symbol))
print (codes)

# list comprehension solution to above: all names are local

codes = [ord(symbol) for symbol in symbols if ord(symbol)%2 == 0]
print (codes)

# may pass list comprehension expression to list()

print (list(ord(symbol) for symbol in symbols if ord(symbol)%2 == 0))
