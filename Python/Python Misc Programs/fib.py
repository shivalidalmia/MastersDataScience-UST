# Shivali Dalmia
# fib.py -> L9-3

def F_iter(n):

    if n < 2:
        fibN = n

    fibN_1 = 1
    fibN_2 = 0

    for count in range(n-1):
        fibN = fibN_1 + fibN_2
        fibN_2 = fibN_1
        fibN_1 = fibN

    return fibN

def F_rec(n):
    # do the same but use recursion: no looping!
    # check for base condition:  n < 2
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return F_rec(n-1) + F_rec(n-2)

def F_rec_fast(n,precomputed):
    if n < 2:
        return n

    if precomputed[n-1] > 0:
        fib_n_1_fast = precomputed[n-1]
    else:
        precomputed[n-1] = F_rec_fast(n - 1,precomputed)
        fib_n_1_fast = precomputed[n-1]

    if precomputed[n-2] > 0:
        fib_n_2_fast = precomputed[n-2]
    else:
        precomputed[n - 2] = F_rec_fast(n - 2,precomputed)
        fib_n_2_fast = precomputed[n - 2]

    return fib_n_1_fast + fib_n_2_fast

def main():
    # finish this

    N = int (input("Enter a int >= 0: "))

    print (f'The {N}th Fibonacci number (iter) is {F_iter(N)}')
    # print (f'The {N}th Fibonacci number (rec) is {F_rec(N)}')

    precomputed = [0] * (N+1)
    print (f'The {N}th Fibonacci number (fast rec) is {F_rec_fast(N,precomputed)}')

    # some interesting patterns:

    print ("The difference is:", F_iter(N)**2 - F_iter(N+1)*F_iter(N-1))
    print ("The ratio: ", F_iter(N) / F_iter(N-1))

main()
