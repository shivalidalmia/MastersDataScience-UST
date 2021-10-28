# Shivali Dalmia
# exp_odd_only.py EC-2
# Assumptions: base (All positive and negative integers) exponent (Only positive integers)

def exp_by_adding(base, exp):
    result = 0

    if exp == 0:
        return 1  # Any number to the power 0 is 1

    if base == 0:
        return 0  # 0 to the power any number is 0 except 0
    elif base < 0 and exp % 2 == 0:
        base = abs(base)  # Any negative base to the even power - result is positive

    temp_base = base

    for exp_count in range(0, exp - 1):
        result = 0
        for add_count in range(abs(base)):
            result += temp_base
        temp_base = result

    return result


def main():
    base = int(input("Enter an int for base value: "))
    exp = int(input("Enter an int for exp value: "))

    result = exp_by_adding(base, exp)

    print(result)

main()
