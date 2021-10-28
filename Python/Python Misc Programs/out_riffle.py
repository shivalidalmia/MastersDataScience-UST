#
# [L8-6] out_riffle.py:
#
# 	Starting code for Lab 8
#

import deck as d

def main():

    the_deck = d.Deck()

    while len(the_deck._cards) > 0:

        original_deck = str(the_deck)
        out_shuffle_count = 0

        # print("before shuffling:", the_deck)

        while True:

            the_deck.out_riffle()
            out_shuffle_count += 1

            if str(the_deck) == original_deck:
                break

        print (f'Deck with {len(the_deck._cards)} returns to original state after {out_shuffle_count} out-shuffles.')

        break # remove this statement to enable iterating over all size Decks

        print("Now removing: ", the_deck.deal_card())  # reduce size by 1

main()