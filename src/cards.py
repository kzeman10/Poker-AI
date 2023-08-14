"""module for defining cards, card sets and deck"""
import enum
import colors


class e_color(enum.Enum):
    """enum for colors"""
    heart = 0
    diamond = 1
    spade = 2
    club = 3


class e_rank(enum.Enum):
    """enum for ranks"""
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9
    ten = 10
    j = 11
    q = 12
    k = 13
    a = 14


letter_to_color = {
    "h": 'heart',
    "d": 'diamond',
    "s": 'spade',
    "c": 'club'
}


class c_card():
    """class representing card"""
    def __init__(self, color=e_color.heart, rank=e_rank.a):
        self.color = color
        self.rank = rank

    def create_from_user(self):
        """createcard from user input"""
        colors.RED = "\033[1;31m"
        colors.NORMAL = "\033[1;30m"
        while True:
            text = input("type help for more info\n" + colors.RED + "card: " + colors.NORMAL).lower()
            if text == "help":
                print("type name of card: color rank")
                print("possible colors: (heart|diamond|spade|club) - you can also use only first letter")
                print("possible ranks: (2|3|4|5|6|7|8|9|10|j|q|k|a)")
                print("example: diamond q")
                print("example: heart 8")
                print("example: h 10")
                continue
            else:
                words = text.split(' ')
                if len(words) == 2:
                    try:
                        if words[0] in letter_to_color:
                            words[0] = letter_to_color[words[0]]
                        self.color = e_color[words[0]]
                        if words[1].isnumeric():
                            self.rank = e_rank(int(words[1]))
                        else:
                            self.rank = e_rank[words[1]]
                        return self
                    except KeyError:
                        pass
                    except ValueError:
                        pass
            print(colors.RED + "I do not understand your answer, try again!\n" + colors.NORMAL)

    def __eq__(self, other) -> bool:
        if self.color == other.color and self.rank == other.rank:
            return True
        return False

    def __lt__(self, other) -> bool:
        if self.rank.value < other.rank.value:
            return True
        return False

    def __hash__(self):
        return hash((self.color, self.rank))


def fill_deck():
    """initialize deck of cards"""
    cards = []
    for color in e_color:
        for rank in e_rank:
            card = c_card(color, rank)
            cards.append(card)
            # print(color, rank)
    return cards


class c_card_sets():
    """class for all cards in the game"""
    def __init__(self):
        self.deck = fill_deck()
        self.hand = []
        self.table = []
        # initialize deck
        # initialize hand
        # transfer card from deck to hand
        print(colors.BLUE + "\nIn this stage all cards on the table are still hidden, but you are supposed to get cards in your hand." + colors.NORMAL)
        print(colors.BLUE + "What are cards in my hand?" + colors.NORMAL)
        # get the card and check if is in the deck
        card = c_card().create_from_user()
        while card not in self.deck:
            print(
                colors.RED + "this card is not in the deck, are you sure?Try another one!" + colors.NORMAL)
            card = c_card().create_from_user()
        print(colors.GREEN + "OK!" + colors.NORMAL)
        self.hand.append(card)
        self.deck.remove(card)
        # get the card and check if is in the deck
        card = c_card().create_from_user()
        while card not in self.deck:
            print(
                colors.RED + "this card is not in the deck, are you sure?Try another one!" + colors.NORMAL)
            card = c_card().create_from_user()
        print(colors.GREEN + "OK!" + colors.NORMAL)
        self.hand.append(card)
        self.deck.remove(card)

    def table_next_stage(self):
        """
        pass a table to the next stage
        (gives or reveals cards)
        """
        if len(self.table) == 0:

            print(colors.BLUE + "\ngoing to next stage" + colors.NORMAL)
            print(colors.BLUE + "In this stage 3 cards on the table should be uncovered" + colors.NORMAL)
            print("reveal 3 cards")
            # get the card and check if is in the deck
            card = c_card().create_from_user()
            while card not in self.deck:
                print(
                    colors.RED + "this card is not in the deck, are you sure?Try another one!" + colors.NORMAL)
                card = c_card().create_from_user()
            print(colors.GREEN + "OK!" + colors.NORMAL)
            self.table.append(card)
            self.deck.remove(card)
            # get the card and check if is in the deck
            card = c_card().create_from_user()
            while card not in self.deck:
                print(
                    colors.RED + "this card is not in the deck, are you sure?Try another one!" + colors.NORMAL)
                card = c_card().create_from_user()
            print(colors.GREEN + "OK!" + colors.NORMAL)
            self.table.append(card)
            self.deck.remove(card)
            # get the card and check if is in the deck
            card = c_card().create_from_user()
            while card not in self.deck:
                print(
                    colors.RED + "this card is not in the deck, are you sure?Try another one!" + colors.NORMAL)
                card = c_card().create_from_user()
            print(colors.GREEN + "OK!" + colors.NORMAL)
            self.table.append(card)
            self.deck.remove(card)
        elif len(self.table) == 3:
            print(colors.BLUE + "\ngoing to next stage" + colors.NORMAL)
            print(colors.BLUE + "In this stage 4 cards on the table should be uncovered" + colors.NORMAL)
            print("reveal 1 card")
            # get the card and check if is in the deck
            card = c_card().create_from_user()
            while card not in self.deck:
                print(
                    colors.RED + "this card is not in the deck, are you sure?Try another one!" + colors.NORMAL)
                card = c_card().create_from_user()
            print(colors.GREEN + "OK!" + colors.NORMAL)
            self.table.append(card)
            self.deck.remove(card)
        elif len(self.table) == 4:
            print(colors.BLUE + "\ngoing to next stage" + colors.NORMAL)
            print(colors.BLUE + "In this stage all 5 cards on the table should be uncovered" + colors.NORMAL)
            print("reveal 1 card")
            # get the card and check if is in the deck
            card = c_card().create_from_user()
            while card not in self.deck:
                print(
                    colors.RED + "this card is not in the deck, are you sure?Try another one!" + colors.NORMAL)
                card = c_card().create_from_user()
            print(colors.GREEN + "OK!" + colors.NORMAL)
            self.table.append(card)
            self.deck.remove(card)
        else:
            print(len(self.table))
            raise ValueError("Wrong number of cards on the table")

    def comb_zero(self):
        """returns combinations of zero cards"""
        return [[]]

    def comb_one(self):
        """returns combinations of one card"""
        result = []
        length = len(self.deck)
        for i in range(length):
            card0 = self.deck[i]
            comb = [card0]
            result.append(comb)
        return result

    def comb_two(self):
        """returns combinations of two cards"""
        result = []
        length = len(self.deck)
        for i in range(length):
            for j in range(i + 1, length):
                card0 = self.deck[i]
                card1 = self.deck[j]
                if card0 != card1:
                    comb = [card0, card1]
                    result.append(comb)
        return result

    def comb_three(self):
        """returns combinations of three cards"""
        result = []
        length = len(self.deck)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    card0 = self.deck[i]
                    card1 = self.deck[j]
                    card2 = self.deck[k]
                    comb = [card0, card1, card2]
                    if len(set(comb)) == len(comb):
                        result.append(comb)
        return result

    def comb_four(self):
        """returns combinations of four cards"""
        result = []
        length = len(self.deck)
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    for ll in range(k + 1, length):
                        card0 = self.deck[i]
                        card1 = self.deck[j]
                        card2 = self.deck[k]
                        card3 = self.deck[ll]
                        comb = [card0, card1, card2, card3]
                        if len(set(comb)) == len(comb):
                            result.append(comb)
        return result

    def get_comb_from_deck(self, n):
        """returns a list of all combinations of n cards, that are in the deck"""
        if n not in [0, 1, 2, 3, 4]:
            raise ValueError("n should be between 0-4")
        functions = [self.comb_zero, self.comb_one, self.comb_two, self.comb_three, self.comb_four]
        return functions[n]()
