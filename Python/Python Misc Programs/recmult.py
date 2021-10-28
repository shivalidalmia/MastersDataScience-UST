# Shivali Dalmia
# recmult.py -> L9-2
# Multiplication using addition and recursion - only

def mult(first,second):
    '''
    return first * second
    == (first-1)*second + second
    '''
    # check for base condition and return if answer is immediate
    if first == 1:
        return second
    else:
        return mult(first-1,second) + second

def main():

    one = int(input("Enter first int >= 0 to multiply: "))
    two = int(input("Enter second int to multiply: "))

    print (f'{one} * {two} == {mult(one,two)}')

main()