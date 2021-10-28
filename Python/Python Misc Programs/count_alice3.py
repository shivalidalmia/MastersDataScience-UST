# Shivali Dalmia
# count_alice3.py -> h7-1

FILENAME = 'alice.txt'

fvar = open(FILENAME, 'r')  # open file for reading

allwords = []  # accumulate the words in this list

for aline in fvar:

    aline = aline.lower()
    aline = aline.replace('.', ' ')
    aline = aline.replace(',', ' ')
    aline = aline.replace('--', ' ')
    aline = aline.replace(':', ' ')
    aline = aline.replace(';', ' ')
    aline = aline.replace('?', ' ')
    aline = aline.replace('!', ' ')
    aline = aline.replace('(', ' ')
    aline = aline.replace(')', ' ')
    aline = aline.replace('"', ' ')
    aline = aline.replace('[', ' ')
    aline = aline.replace(']', ' ')
    aline = aline.replace('_', ' ')

    words = aline.split()

    allwords.extend(words)

filtered_allwords = []

for word in allwords:

    if word == "'":
        pass
    elif word == "'tis":
        filtered_allwords.append(word)
    elif word == "''tis":
        filtered_allwords.append(word[1:])
    elif word == "'em":
        filtered_allwords.append(word)
    else:
        left_quote_loc = word.find("'")     # Reading left most occurrence of (')
        right_quote_loc = word.rfind("'")  # Reading right most occurrence of (')

        if left_quote_loc == 0 and right_quote_loc == len(word) - 1:  # Removing (') quote from words like 'well'
            filtered_allwords.append(word[1:-1])
        elif left_quote_loc == 0:               # Removing (') quote from words like 'well
            filtered_allwords.append(word[1:])
        elif right_quote_loc == len(word) - 1:  # Removing (') quote from words like jury-men'
            filtered_allwords.append(word[:-1])
        elif 0 < left_quote_loc < len(word) - 1:  # Appending word if (') quote is between like they're
            filtered_allwords.append(word)
        else:
            filtered_allwords.append(word)

# Dictionary word_counts to count each word in filtered_allwords

word_counts = {}

for word in filtered_allwords:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

keys = list(word_counts.keys())
keys.sort()

for next_key in keys:
    print("%15s - %d" % (next_key, word_counts[next_key]))

fvar.close()


# First 20 and last 20 lines of output

'''
            'em - 3
           'tis - 5
              0 - 1
              3 - 1
              a - 631
        a-piece - 1
          abide - 1
           able - 1
          about - 94
          above - 3
        absence - 1
         absurd - 2
     acceptance - 1
       accident - 2
   accidentally - 1
        account - 1
     accounting - 1
       accounts - 1
     accusation - 1
     accustomed - 1
             ye - 1
           year - 2
          years - 1
         yelled - 1
           yelp - 1
            yer - 4
            yes - 13
      yesterday - 3
            yet - 25
            you - 365
          you'd - 10
         you'll - 6
         you're - 23
         you've - 7
          young - 5
           your - 62
          yours - 3
       yourself - 10
          youth - 6
        zealand - 1
         zigzag - 1
'''