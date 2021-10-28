# Shivali Dalmia
# recursive_validate.py -> demo for L9-2
# Prompt and read int until one > 0 is entered, then return

def read_pos():
    number = int(input ("Please enter an int > 0: "))
    if number > 0:
        return number
    # try again => recursion is equivalent to looping...
    return read_pos()

def main():
    print (read_pos())

main()