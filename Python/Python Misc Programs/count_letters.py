"""
Shivali Dalmia
count_letters.py -> L7-1
Print out frequency counts of all letters 'a'..'z', 'A'..'Z' found in input string.
Only counts >0 should be printed.
"""

import string

in_string = input("Enter a string to count its upper+lower case letters: ")

print("You entered '%s'" % in_string)

counts = {}  # Initialize new dictionary (counts) to empty

for ch in in_string:

    # Approach1
    if ch in string.ascii_letters:
        if counts.get(ch,0) == 0:
            counts[ch] = 1
        else:
            counts[ch] += 1

counts_keys_list = list(counts.keys())
counts_keys_list.sort()                  # Sorting the keys list

for key in counts_keys_list:             # Printing final list
    print(f"{key} - {counts[key]}")

