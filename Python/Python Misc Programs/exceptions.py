"""
Shivali Dalmia
exceptions.py -> L7-2
"""

class NegativeValueError(Exception):            # Creating a user defined exception for negative values
    errorMessage = "float must be > 0.0."

def read_pos_float():

    float_str = float(input("Enter a float > 0.0: "))

    if float_str > 0.0:
        return float_str
    else:
        raise NegativeValueError

def main():

    while True:

        try:
            returned = read_pos_float()
            print('You entered:', returned)
            break
        except ValueError:                   # Catch ValueError exception if entered value is not float
            print("Not a valid float")
        except NegativeValueError:                    # Catch User Defined Exception if float value entered is negative
            print(NegativeValueError.errorMessage)
        except Exception:
            print("Not a valid input")

        print("Please reenter.")

main()
