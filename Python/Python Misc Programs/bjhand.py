# Shivali Dalmia
#  bjhand.py -> L8-5
#  Create subclass BJHand of Hand with is_blackjack() method

import card
import deck
import hand

class BJHand(hand.Hand):
    """
    BJHand extends superclass Hand
        adding is_blackjack() method
    """

    def __init__(self):
        '''
        Initialize Hand:
          first call superclass Hand's __init__()
          using special super() function:
          this initializes Hand's _cards_in_hand field
        '''
        super().__init__() # needed to set the superclass instance attributes

    def __str__(self):
        '''
        Return str "Blackjack hand:\t" prepended to result
            returned by Hand.__str__()
        '''
        return "Blackjack hand:\t" + super().__str__()
            # note how subclass methods can call overridden superclass methods

    def is_blackjack(self):
        '''
        check if this hand is Blackjack, returning True;
            False otherwise
        '''
        # if the FIRST card (self._cards_in_hand[0]) has an ace and
        #    the SECOND (self._cards_in_hand[1]) has a 10, J, Q, or K:
        #       return True
        # else:
        #     return False
        if (self._cards_in_hand[0]._rank == 1 and self._cards_in_hand[1]._rank in [10, 11, 12, 13]) or \
                (self._cards_in_hand[1]._rank == 1 and self._cards_in_hand[0]._rank in [10, 11, 12, 13]):
            return True
        else:
            return False


def main():

    TRIALS = 1000000
    double_blackjack_count = 0 # accumulator of # of blackjack hands

    for count in range(TRIALS):

        new_deck = deck.Deck()
        new_deck.shuffle()

        # create two new Hands, hand_1 and hand_2
        hand1 = BJHand()
        hand2 = BJHand()

        # deal card1 from new_deck and add to hand_1
        card1 = new_deck.deal_card()
        hand1.add_card(card1)

        # deal card2 from new_deck and add to hand_2
        card2 = new_deck.deal_card()
        hand2.add_card(card2)

        # deal card3 from new_deck and add to hand_1
        card3 = new_deck.deal_card()
        hand1.add_card(card3)

        # deal card4 from new_deck and add to hand_2
        card4 = new_deck.deal_card()
        hand2.add_card(card4)


        # Checking blackjack for hand1
        if hand1.is_blackjack():
            # Checking blackjack for hand2
            if hand2.is_blackjack():
                double_blackjack_count += 1


    print (f'Both hands have Blackjack {double_blackjack_count} times.')

    print (f'Percentage of double blackjacks: {100.0*double_blackjack_count/TRIALS}')


if __name__ == "__main__":
    main()
