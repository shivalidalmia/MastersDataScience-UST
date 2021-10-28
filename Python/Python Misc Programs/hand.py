# Shivali Dalmia
#  hand.py -> L8-2
#  Class that represents a hand of Cards

import card as c
import deck as d

class Hand():
    """
    Hand represents an ordered list of 0 or more Cards,
    with one list attribute: _cards_in_hand
    Each card in the hand has its Card ref as an element of _cards_in_hand.
    """

    def __init__(self):
        self._cards_in_hand = []

    def __str__(self):
        card_str = ''
        for card in self._cards_in_hand:
            card_str = card_str + str(card) + '\t'
        return card_str

    def add_card(self,card_to_add):
        self._cards_in_hand.append(card_to_add)

def main():

    new_deck = d.Deck()
    new_deck.shuffle()

    hand1 = Hand()
    hand2 = Hand()

    # Adding cards alternately to hand1 and hand2
    for count in range(1,11):
        if count%2 != 0:
            hand1.add_card(new_deck.deal_card())
        else:
            hand2.add_card(new_deck.deal_card())

    print(hand1)
    print(hand2)

if __name__ == "__main__":
    main()
