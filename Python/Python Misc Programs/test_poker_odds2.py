'''
Shivali Dalmia
test_poker_odds2.py -> H7-2
'''

import random

# The following two lists of str are used to translate from internal int
#   representation to external string equivalent

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["", "Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
         'Eight', "Nine", "Ten", "Jack", "Queen", "King"]


# Here's two Python classes: Card's objects represent a playing card
#   and Deck objects represent a single deck of such cards

class Card():
    """
    Represents a single playing card,
        whose rank internally is int _rank: 1..13 => "Ace".."King"
        and whose suit internally is int _suit 0..3 => "Clubs".."Spades"
    """

    def __init__(self, rank=1, suit=3):  # this is the constructor!

        '''
        Initialize card with given int suit and int rank
        '''
        self._rank = rank
        self._suit = suit

    def __str__(self):  # this is the "stringifier" or cast operator

        """
        Return the string name of this card:
        "Ace of Spades": translates int fields to strings
        """

        # Example:
        #
        # "Ace of Spades" is returned if self._rank==1, self._suit==3

        str_to_return = RANKS[self._rank] + " of " + SUITS[self._suit]

        return str_to_return


class Deck():
    """
    Represents a deck of 52 standard playing cards,
        as an internal field referencing a list of Card refs
    """

    def __init__(self):  # constructor

        """
        Initialize deck: field _cards is list containing
            52 Card refs, initially
        """

        self._cards = []

        for rank in range(1, 14):
            for suit in range(4):
                c = Card(rank, suit)  # create next Card with given value
                self._cards.append(c)  # add it to this Deck

    def __str__(self):

        """
        "Stringified" deck: string of Card named,
        with \n for easier reading
        """
        str_to_return = ''  # accumulate each card's str() description, separated by '\n'

        # for index in range(len(self._cards)):
        #     self._cards[index]

        for c in self._cards:
            temp = str(c)  # temp is the stringified card
            str_to_return = str_to_return + temp + "\n"  # note \n at end

        return str_to_return

    def shuffle(self):
        random.shuffle(self._cards)  # note random function that does this

    def deal_card(self):
        to_return = self._cards.pop(0)  # get and remove top card from deck
        return to_return


def build_rank_dict(hand):
    rdict = {}

    for card in hand:
        rdict[card._rank] = rdict.get(card._rank, 0) + 1

    return rdict

def is_hand_sequential(rdict):

    is_sequential = False
    rdict_ranks_list = list(rdict.keys())
    rdict_ranks_list.sort()

    # Check if card ranks are consecutive (difference between them is one)
    for index in range(1, len(rdict_ranks_list)):
        difference = rdict_ranks_list[index] - rdict_ranks_list[index - 1]
        if difference == 1:
            is_sequential = True
            continue
        else:
            is_sequential = False
            break

    return is_sequential

def is_hand_of_same_suit(hand):

    # Check if ranks belong to same suit
    # If occurrence of first value of suit list
    # is equal to number of cards then all suits are same

    suit_list = [item.__dict__['_suit'] for item in hand]
    count_of_first_elt = suit_list.count(suit_list[0])
    if count_of_first_elt == len(suit_list):
        return True
    else:
        return False

def is_royal_fulsh_sequence(rdict):

    is_royal_flush = False
    rdict_list = list(rdict.keys())
    rdict_list.sort()
    if rdict_list == [1, 10, 11, 12, 13]:
        is_royal_flush = True

    return is_royal_flush

def has_one_pair(rdict):
    pair_count = 0
    three_count = 0
    for v in rdict.values():
        if v == 2:
            pair_count += 1
        elif v == 3:
            three_count += 1

    if pair_count == 1 and three_count != 1:
        return True
    else:
        return False


def has_two_pairs(rdict):
    pair_count = 0
    for v in rdict.values():
        if v == 2:
            pair_count += 1

    if pair_count == 2:
        return True
    else:
        return False

def has_three_of_a_kind(rdict):

    pair_count = 0
    three_count = 0
    for v in rdict.values():
        if v == 3:
            three_count += 1
        elif v==2:
            pair_count +=1

    if three_count == 1 and pair_count != 1:
        return True
    else:
        return False


def has_full_house(rdict):

    pair_count = 0
    three_count = 0
    for v in rdict.values():
        if v == 2:
            pair_count += 1
        elif v == 3:
            three_count += 1

    if pair_count == 1 and three_count == 1:
        return True
    else:
        return False

def has_four_of_a_kind(rdict):

    four_count = 0
    for v in rdict.values():
        if v == 4:
            four_count += 1

    if four_count == 1:
        return True
    else:
        return False

def has_straight(rdict,hand):

    if not is_royal_fulsh_sequence(rdict) and is_hand_sequential(rdict) and not is_hand_of_same_suit(hand):
        return True
    else:
        return False

def has_flush(rdict,hand):

    if not is_royal_fulsh_sequence(rdict) and not is_hand_sequential(rdict) and is_hand_of_same_suit(hand):
        return True
    else:
        return False

def has_straight_flush(rdict,hand):

    if not is_royal_fulsh_sequence(rdict) and is_hand_of_same_suit(hand) and is_hand_sequential(rdict):
            return True
    else:
        return False


def has_royal_flush(rdict,hand):

    is_royal_flush = False
    rdict_list = list(rdict.keys())
    rdict_list.sort()

    if rdict_list == [1,10,11,12,13] and is_hand_of_same_suit(hand):
        is_royal_flush = True

    return is_royal_flush


def card_example():  # call this by editing code below

    """
        Test the Card class:
        Create default Card, then another
        Try printing str version of Card three different ways...
    """

    card1 = Card()  # Card(1,3) => Ace of Clubs
    card2 = Card(12, 2)  # Card (12,2) => Queen of Hearts

    card1._newfield = 47  # we can add new fields to any Python object!

    #
    # Three ways of printing a Card
    #

    print(card1.__str__())  # calling the methods against card
    print(str(card2))  # type-casting
    print(card2)  # short-cut: passing obj ref to print does str() automagically

    print(card1._newfield)  # see the new field value?

    print(card1._rank)  # see the rank (1..13)
    print(card1._suit)  # see the suit (0..3)


def deck_example():  # call this by editing code below

    """
    Test the Deck class:
    Create, print then shuffle, print again
    Then deal first two cards and print, along with bottom card
    """

    deck = Deck()
    print(str(deck))  # print entire deck before shuffling

    print("Now we shuffle:\n")

    deck.shuffle()
    print(str(deck))  # print entire deck after shuffling

    card1 = deck.deal_card()
    card2 = deck.deal_card()

    print("The first card dealt is", str(card1), "and the second is", str(card2))
    print("Bottom of deck is", deck._cards[-1])


def main():

    TRIALS = int(input ("Input number of hands to test: "))

    hand = []  # list of Card refs in the hand

    one_pair_count = 0
    two_pair_count = 0
    three_count = 0
    four_count = 0
    full_house_count = 0
    straight_count = 0
    flush_count = 0
    straight_flush_count = 0
    royal_flush_count = 0

    for num in range(TRIALS):

        d = Deck()
        d.shuffle()
        hand = []

        for count in range(5):
            hand.append(d.deal_card())

        rank_dict = build_rank_dict(hand)

        if has_one_pair(rank_dict):     # Checking one_pair
            one_pair_count += 1

        elif has_two_pairs(rank_dict):  # Checking two-pair
            two_pair_count += 1

        elif has_three_of_a_kind(rank_dict): # Checking three-of-a-kind
            three_count += 1

        elif has_four_of_a_kind(rank_dict):  # Checking four-of-a-kind
            four_count += 1

        elif has_full_house(rank_dict):      # Checking full house
            full_house_count += 1

        elif has_straight(rank_dict,hand):   # Checking straight
            straight_count += 1

        elif has_flush(rank_dict,hand):      # Checking flush
            flush_count += 1

        elif has_straight_flush(rank_dict,hand):  # Checking straight flush
            straight_flush_count += 1

        elif has_royal_flush(rank_dict,hand):     # Checking royal flush
            royal_flush_count += 1

    print(f"Expected:42.2569%  Number / % of one pair hands is: {one_pair_count} / %{100.0 * one_pair_count / TRIALS}")

    print(f"Expected:4.7539%   Number / % of two pair hands is: {two_pair_count} / %{100.0 * two_pair_count / TRIALS}")

    print(f"Expected:2.1128%   Number / % of 3-of-a-kind hands is: {three_count} / %{100.0 * three_count / TRIALS}")

    print(f"Expected:0.0240%   Number / % of 4-of-a-kind hands is: {four_count} / %{100.0 * four_count / TRIALS}")

    print(f"Expected:0.1441%   Number / % of full house hands is: {full_house_count} / %{100.0 * full_house_count / TRIALS}")

    print(f"Expected:0.3925%   Number / % of straight hands is: {straight_count} / %{100.0 * straight_count / TRIALS}")

    print(f"Expected:0.1965%   Number / % of flush hands is: {flush_count} / %{100.0 * flush_count / TRIALS}")

    print(f"Expected:0.00139%  Number / % of straight flush hands is: {straight_flush_count} / %{100.0 * straight_flush_count / TRIALS}")

    print(f"Expected:0.000154% Number / % of royal flush hands is: {royal_flush_count} / %{100.0 * royal_flush_count / TRIALS}")


if __name__ == "__main__":

    main()


# -------------------------------------------------------------------------
# Pytest tests for testing all types of hands
# -------------------------------------------------------------------------

def test_one_pair_1():
    # a hand with Ace of Clubs, Ace of Spades, Two of Clubs, Three of Clubs, Four of Clubs

    testhand = [Card(1, 0), Card(1, 3),
                Card(2, 0), Card(3, 0),
                Card(4, 0)]

    rdict = build_rank_dict(testhand)

    assert has_one_pair(rdict)


def test_one_pair_2():
    testhand = [Card(2, 3), Card(1, 2),
                Card(3, 1), Card(13, 2),
                Card(2, 0)]

    rdict = build_rank_dict(testhand)

    assert has_one_pair(rdict)

def test_one_pair_3():
    testhand = [Card(4, 3), Card(1, 2),
                Card(3, 1), Card(13, 2),
                Card(4, 0)]

    rdict = build_rank_dict(testhand)

    assert has_one_pair(rdict)


def test_two_pairs_1():
    testhand = [Card(2, 3), Card(3, 2),
                Card(3, 1), Card(13, 2),
                Card(2, 0)]

    rdict = build_rank_dict(testhand)

    assert has_two_pairs(rdict)

def test_two_pairs_2():
    testhand = [Card(4, 3), Card(1, 2),
                Card(4, 1), Card(13, 2),
                Card(1, 0)]

    rdict = build_rank_dict(testhand)

    assert has_two_pairs(rdict)

def test_two_pairs_3():
    testhand = [Card(12, 3), Card(3, 2),
                Card(3, 1), Card(13, 2),
                Card(12, 0)]

    rdict = build_rank_dict(testhand)

    assert has_two_pairs(rdict)

def test_three_of_a_kind_1():
    testhand = [Card(12, 3), Card(3, 2),
                Card(12, 1), Card(12, 2),
                Card(1, 0)]

    rdict = build_rank_dict(testhand)

    assert has_three_of_a_kind(rdict)

def test_three_of_a_kind_2():
    testhand = [Card(10, 3), Card(10, 2),
                Card(12, 1), Card(10, 0),
                Card(1, 0)]

    rdict = build_rank_dict(testhand)

    assert has_three_of_a_kind(rdict)

def test_three_of_a_kind_3():
    testhand = [Card(1, 3), Card(10, 2),
                Card(12, 1), Card(1, 2),
                Card(1, 0)]

    rdict = build_rank_dict(testhand)

    assert has_three_of_a_kind(rdict)

def test_four_of_a_kind_1():
    testhand = [Card(1, 3), Card(1, 2),
                Card(1, 1), Card(1, 0),
                Card(11, 0)]

    rdict = build_rank_dict(testhand)

    assert has_four_of_a_kind(rdict)

def test_four_of_a_kind_2():
    testhand = [Card(13, 3), Card(13, 2),
                Card(13, 1), Card(13, 0),
                Card(11, 0)]

    rdict = build_rank_dict(testhand)

    assert has_four_of_a_kind(rdict)

def test_four_of_a_kind_3():
    testhand = [Card(2, 3), Card(2, 4),
                Card(2, 1), Card(2, 0),
                Card(11, 0)]

    rdict = build_rank_dict(testhand)

    assert has_four_of_a_kind(rdict)

def test_straight_1():
    testhand = [Card(2, 3), Card(3, 4),
                Card(4, 1), Card(5, 0),
                Card(6, 0)]

    rdict = build_rank_dict(testhand)

    assert has_straight(rdict,testhand)

def test_straight_2():
    testhand = [Card(9, 3), Card(12, 4),
                Card(13, 1), Card(10, 0),
                Card(11, 0)]

    rdict = build_rank_dict(testhand)

    assert has_straight(rdict,testhand)

def test_straight_3():
    testhand = [Card(1, 3), Card(2, 4),
                Card(3, 1), Card(4, 0),
                Card(5, 0)]

    rdict = build_rank_dict(testhand)

    assert has_straight(rdict,testhand)

def test_flush_1():
    testhand = [Card(1, 0), Card(2, 0),
                Card(9, 0), Card(4, 0),
                Card(5, 0)]

    rdict = build_rank_dict(testhand)

    assert has_flush(rdict,testhand)

def test_flush_2():
    testhand = [Card(10, 3), Card(2, 3),
                Card(1, 3), Card(4, 3),
                Card(11, 3)]

    rdict = build_rank_dict(testhand)

    assert has_flush(rdict,testhand)

def test_flush_3():
    testhand = [Card(4, 4), Card(2, 4),
                Card(9, 4), Card(10, 4),
                Card(5, 4)]

    rdict = build_rank_dict(testhand)

    assert has_flush(rdict,testhand)

def test_flush_3():
    testhand = [Card(4, 4), Card(2, 4),
                Card(9, 4), Card(10, 4),
                Card(5, 4)]

    rdict = build_rank_dict(testhand)

    assert has_flush(rdict,testhand)

def test_straight_flush_1():
    testhand = [Card(1, 4), Card(2, 4),
                Card(3, 4), Card(4, 4),
                Card(5, 4)]

    rdict = build_rank_dict(testhand)

    assert has_straight_flush(rdict,testhand)

def test_straight_flush_2():
    testhand = [Card(7, 2), Card(8, 2),
                Card(11, 2), Card(9, 2),
                Card(10, 2)]

    rdict = build_rank_dict(testhand)

    assert has_straight_flush(rdict,testhand)

def test_straight_flush_3():
    testhand = [Card(9, 0), Card(13, 0),
                Card(11, 0), Card(12, 0),
                Card(10, 0)]

    rdict = build_rank_dict(testhand)

    assert has_straight_flush(rdict,testhand)

def test_royal_flush_1():
    testhand = [Card(1, 0), Card(13, 0),
                Card(11, 0), Card(12, 0),
                Card(10, 0)]

    rdict = build_rank_dict(testhand)

    assert has_royal_flush(rdict,testhand)

def test_royal_flush_2():
    testhand = [Card(1, 1), Card(13, 1),
                Card(11, 1), Card(12, 1),
                Card(10, 1)]

    rdict = build_rank_dict(testhand)

    assert has_royal_flush(rdict,testhand)

def test_royal_flush_3():
    testhand = [Card(1, 4), Card(13, 4),
                Card(11, 4), Card(12, 4),
                Card(10, 4)]

    rdict = build_rank_dict(testhand)

    assert has_royal_flush(rdict,testhand)

