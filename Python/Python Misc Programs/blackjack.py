# Shivali Dalmia
# blackjack.py -> L8-4
# Experimental odds of drawing two Blackjack hands from
#       top 4 cards of Deck

import deck
import hand
import bjhand

TRIALS = 100000


def main():

    blackjack_count = 0 # accumulator of # of blackjack hands

    for count in range(TRIALS):

        new_deck = deck.Deck()
        new_deck.shuffle()

        # create two new Hands, hand_1 and hand_2
        hand1 = bjhand.BJHand()
        hand2 = bjhand.BJHand()

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

        # if hand_1 and hand_2 are both Blackjack (one Ace, one face or 10 card),
        #   add 1 to both_aces_count

        # Checking blackjack for hand1
        # if (hand1._cards_in_hand[0]._rank == 1 and hand1._cards_in_hand[1]._rank in [10,11,12,13]) or \
        #         (hand1._cards_in_hand[1]._rank == 1 and hand1._cards_in_hand[0]._rank in [10,11,12,13]):
        #
        #     # Checking blackjack for hand2
        #     if (hand2._cards_in_hand[0]._rank == 1 and hand2._cards_in_hand[1]._rank in [10,11,12,13]) or \
        #             (hand2._cards_in_hand[1]._rank == 1 and hand2._cards_in_hand[0]._rank in [10,11,12,13]):
        #         blackjack_count += 1b

        if hand1.is_blackjack() and hand2.is_blackjack():
            blackjack_count += 1


    print (blackjack_count)

    print (f"Percentage of blackjacks: {100.0*blackjack_count/TRIALS}")


main()
