#
#  L9-5.3: sum_multiples_3.py (no submission required)
#
# Now we define sum() recursively for lists: look, no state!
#   (but no filtering, so all ints 1..9 are summed - for now)

def sumr(seq):
    if len(seq) == 0:
        return 0
    return seq[0] + sumr(seq[1:])

print (sumr([k for k in range(1,10)])) # using a list comprehension

# We can define a sequence of values recursively:
# note use of passed function filter_func:
#   functional programming makes functions first-class data

def until(n, filter_func, v):
    if v == n:
        return []
    if filter_func(v):
        return [v] + until(n, filter_func, v+1)
    else:
        return until(n, filter_func, v+1)

mult_3_5 = lambda n: n%3==0 or n%5==0 # => a function without a name!

print ("until(...) returns a list...")

print(until (10, mult_3_5, 0))
print(until (10, lambda n: n%3==0 or n%5==0, 0))

print ("Using our sumr composed with until, filtered by lambda...")
print(sumr(until (10, lambda n: n%3==0 or n%5==0, 0)))

