# Shivali Dalmia
# two_aces.py -> L8-1
# Experimental % of drawing two aces in a row from a shuffled Deck

import deck

TRIALS = 100000


def main():
    two_aces_count = 0

    for count in range(TRIALS):
        new_deck = deck.Deck()

        new_deck.shuffle()

        card1 = new_deck.deal_card()
        card2 = new_deck.deal_card()

        if card1._rank == 1 and card2._rank == 1: # Checking for two aces
            two_aces_count += 1

    print (two_aces_count)
    print (100.0 * two_aces_count / TRIALS)


main()
