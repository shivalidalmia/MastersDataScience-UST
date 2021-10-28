''''
Assume you have two dictionaries d1 and d2, which have both been initialized.

Write code to create a new dictionary ddiff from d1 and d2 having the following properies:

(a) k is a key in ddiff if and only if  k is a key in only one of the two dictionaries d1 and d2.

(b) The value of k in ddiff is the same as its value in whichever of d1 and d2 it is a key.

Thus, if k is a key in only d1, then its value in ddiff should be the same as its value in d1.
Similarly, if k is a key in only d2, then its value in ddiff should also be the same as its value in d2.
'''

def diff(d1,d2):
    ddiff_dict = {}

    for key in d1.keys():
        if key not in d2 and key not in ddiff_dict:
            ddiff_dict[key] = d1[key]

    for key in d2.keys():
        if key not in d1 and key not in ddiff_dict:
            ddiff_dict[key] = d2[key]

    return ddiff_dict

def main():
    d1 = {"a": 1, "b": 2, "c": 3,"f":6}
    d2 = {"a": 1,"b":11, "d": 2, "e": 10, "f":5}
    ddiff = diff(d1,d2)
    print(ddiff)

main()
