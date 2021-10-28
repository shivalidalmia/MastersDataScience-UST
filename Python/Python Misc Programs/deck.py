#  Shivali Dalmia
#  deck.py
#  Part of Lab 8

import random
import card as ca
import hand as h


class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as a list of Card refs
    """

    def __init__(self):
        '''
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        :return: nothing
        '''

        self._cards = []
        for rank in range(1, 14):
            for suit in range(4):
                c = ca.Card(rank, suit)
                self._cards.append(c)

    def __str__(self):
        '''
        "Stringified" deck: string of all Card names,
        in deck order separated by '\n' for easier reading
        '''

        deck_str_to_return = ''

        # visit every card in deck this way:
        #
        # for index in range(len(self._cards)):
        #     self._cards[index]
        #
        # but it's easier to do it as follows:

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            deck_str_to_return = deck_str_to_return + temp + "\n"  # note \n at end

        return deck_str_to_return

    def shuffle(self):
        random.shuffle(self._cards)  # note random function to do this

    def deal_card(self):
        top_card = self._cards.pop(0)  # get and remove top card from deck
        return top_card

    def deal_hand(self):

        new_hand = h.Hand()
        for count in range(5):
            try:
                c = self.deal_card()
                new_hand.add_card(c)
            except IndexError:
                self.__init__()
                self.shuffle()
                c = self.deal_card()
                new_hand.add_card(c)

        return new_hand

    ### L8-6 (complete code): add new method out_riffle()

    def out_riffle(self):

        # create two empty lists

        top_half = []
        bottom_half = []

        # save # cards in deck

        cards_in_deck = len(self._cards)

        # copy the first half of self._cards into top_half:
        #   (loop cards_in_deck//2 times, deal from deck and append to top_half))

        top_half = self._cards[:(len(self._cards)+1)//2]

        # copy the remaining self._cards into bottom_half

        bottom_half = self._cards[(1 + len(self._cards)) // 2:]

        # now copy back into new_cards list,
        #   doing perfect out shuffle via alternation

        # note the use of slices to make this easy!

        self._cards[0::2] = top_half
        self._cards[1::2] = bottom_half

def main():
    '''
    Create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    '''

    deck = Deck()
    print(str(deck))

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck))

    card_1 = deck.deal_card()
    card_2 = deck.deal_card()

    print("The first card dealt is", card_1, "and the second is", card_2)
    print("Bottom of deck is", deck._cards[-1])  # can't hide the implementation!


# only run main() if we're not importing it...
if __name__ == "__main__":
    main()
