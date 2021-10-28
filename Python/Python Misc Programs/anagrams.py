"""
Shivali Dalmia
anagrams.py -> L7-4
Find and print all words in the largest set of words that are all anagrams of each other
    == "anagram lists"
"""

def make_sorted(word):
    char_list = list(word)
    char_list.sort()
    sort_done = ''.join(char_list)
    return sort_done

word_file = open("words_2.txt", "r")

anagrams = {}

for word in word_file:

    word = word.rstrip('\n')  # Stripping new line character
    alpha_sort = make_sorted(word) # Sort the word in ascending of characters

    if alpha_sort in anagrams:
        anagrams[alpha_sort].append(word)
    else:
        anagrams[alpha_sort] = [word]

print(anagrams)

input("ENTER to continue:") # pause to allow browsing of output

word_file.close()

anagram_freq = []

# Counting frequency of anagrams for each key in anagrams dictionary
for key in anagrams.keys():
    anagram_freq.append((len(anagrams[key]),anagrams[key]))

# Sorting in descending order of length of anagrams
anagram_freq.sort(reverse=True)

# Printing anagram list values with maximum words (top 20)
for elt in anagram_freq[:20]:
    print(elt)
