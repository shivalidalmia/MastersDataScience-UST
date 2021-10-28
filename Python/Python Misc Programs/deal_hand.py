# Shivali Dalmia
#  deal_hand.py -> L8-3
#   Modify Deck.deal_hand() as described in handout:
#       trying to deal from an empty Deck should
#       be handled with try...except by
#       'refilling' the Deck's _cards list
#       with a new list of 52 standard cards
#
#   The test code below is complete and when run should NOT
#       cause any exceptions to halt the program.
#

import deck as d


def main():

    the_deck = d.Deck()

    for count in range(11):
        hand = the_deck.deal_hand()  # last hand will empty the_deck: should not crash!

        print(hand) # str(hand) is implied with print()

main()
