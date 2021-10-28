# Shivali Dalmia
# taxes.py EC-1

def calculateTax(income):

    tax = 0

    if 0<= income <=9875:
        tax = 0.10*income       # 10% for 0-$9,875
    elif 9876<= income <=40125:
        tax = 0.12*income       # 12% for $9,875-$40,125
    elif 40126<= income <=85525:
        tax = 0.10*9875 + 0.12*(40125-9875) + 0.22*(income-40125)  # 22% for $40,126-$85,525
    elif 85526<= income <= 163300:
        tax = 0.24*income           # 24% for $85,526-$163,300
    elif 163301<= income <=207350:
        tax=0.32*income             # 32% for $163,301-$207,350
    elif 207351<= income <=518400:
        tax=0.35*income             # 35% for $207,351-$518,400
    elif income>=518401:
        tax=0.37*income             # 37% for $518,401+

    return round(tax,2)

def main():
    income = float(input("Enter your income in float: "))

    if income>=0.0:                 # Valid income
        tax = calculateTax(income)
        print(tax)
    else:                           # Invalid income
        print("Bad input")

main()
