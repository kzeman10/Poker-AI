"""module for evaluating combinations"""
import enum
import random


class e_evaluation(enum.Enum):
    """enum for all evaluations of combination of cards"""
    pair = 0
    two_pair = 1
    triple = 2
    straight = 3
    flush = 4
    full_house = 5
    quartet = 6
    straight_flush = 7


def check_pair(cards):
    """
    goes through card and for each one check if has some pair,
    if not, delete it
    """
    tmp = cards.copy()
    for _ in range(len(tmp) - 1):
        for j in range(1, len(tmp)):
            if tmp[0].rank == tmp[j].rank:
                return True, tmp[0].rank
        tmp.pop(0)
    return False


def check_triple(cards):
    """
    goes through card and for each one check if has some pair,
    if not, delete it
    if yes, repeat
    """
    tmp = cards.copy()
    for _ in range(len(tmp) - 2):
        for j in range(1, len(tmp)):
            # uncomment this print to see how it works
            # print(0, j)
            if tmp[0].rank == tmp[j].rank:
                for k in range(j + 1, len(tmp)):
                    # goes there only if pair was found and there are still some cards left to be in tripple
                    # uncomment this print to see how it works
                    # print(0, j, k)
                    if tmp[0].rank == tmp[k].rank:
                        return True, tmp[0].rank
        tmp.pop(0)
    return False


def checkquartet_second_part(tmp, j):
    """second part of quartet check"""
    for k in range(j + 1, len(tmp)):
        # goes there only if pair was found and there are still some cards left to be in tripple
        # uncomment this print to see how it works
        # print(0, j, k)
        if tmp[0].rank == tmp[k].rank:
            for ll in range(k + 1, len(tmp)):
                # goes there only if tripple was found and there are still some cards left to be in tripple
                # uncomment this print to see how it works
                # print(0, j, k, l)
                if tmp[0].rank == tmp[ll].rank:
                    return True, tmp[0].rank
    return False, None


def checkquartet(cards):
    """checks set of cards for quartet"""
    tmp = cards.copy()
    for _ in range(len(tmp) - 3):
        for j in range(1, len(tmp)):
            if tmp[0].rank == tmp[j].rank:
                a = checkquartet_second_part(tmp, j)
                if a[0]:
                    return a
        tmp.pop(0)
    return False, None


def delete_pair(cards):
    """delete first pair, that is found in the list"""
    tmp = cards.copy()
    result = cards.copy()
    for _ in range(len(tmp) - 1):
        for j in range(1, len(tmp)):
            # print(0, j)
            if tmp[0].rank == tmp[j].rank:
                result.remove(tmp[0])
                result.remove(tmp[j])
                return result
        tmp.pop(0)
    raise ValueError("there is no pair")


def delete_triple(cards):
    """
    delete first triple found in the list
    goes through card and for each one check if has some pair,
    if not, delete it
    if yes, repeat
    """
    tmp = cards.copy()
    result = cards.copy()
    for _ in range(len(tmp) - 2):
        for j in range(1, len(tmp)):
            # uncomment this print to see how it works
            # print(0, j)
            if tmp[0].rank == tmp[j].rank:
                for k in range(j + 1, len(tmp)):
                    # goes there only if pair was found and there are still some cards left to be in tripple
                    # uncomment this print to see how it works
                    # print(0, j, k)
                    if tmp[0].rank == tmp[k].rank:
                        result.remove(tmp[0])
                        result.remove(tmp[j])
                        result.remove(tmp[k])
                        return result
        tmp.pop(0)
    raise ValueError("there is no tripple")


def checkflush(cards):
    """divide colors into boxes and check, if there is more than 5 in one box"""
    colors = [0, 0, 0, 0]
    for card in cards:
        colors[card.color.value] += 1
        if colors[card.color.value] >= 5:
            return True
    return False


def find_highest_in_color(cards):
    """find highest card in dominant color"""
    colors = [0, 0, 0, 0]
    for card in cards:
        colors[card.color.value] += 1
        if colors[card.color.value] >= 5:
            dominant_color = card.color

    tmp = cards.copy()
    tmp.sort(reverse=True)
    for card in tmp:
        if card.color == dominant_color:
            return card.rank
    raise ValueError("no card has dominant color")


def check_straight(cards):
    """check if there is sequence of 5 cards after each other"""
    # sort by rank, overrided operator < of c_card
    tmp = cards.copy()
    tmp.sort()
    # get last value -1 for first card to be counted as part of the sequence
    last_value = tmp[0].rank.value - 1
    straight = 0
    for card in tmp:
        if card.rank.value != last_value:
            if card.rank.value == last_value + 1:
                straight += 1
                if straight >= 5:
                    return True, card.rank
                last_value = card.rank.value
            else:
                straight = 1
                last_value = card.rank.value
    return False


def check_straight_flush(cards):
    """
    checking, for straight flush
    this function must be called after checking positive for flush and straight
    """

    # get dominant color is the set
    colors = [0, 0, 0, 0]
    # dominant_color = e_color.heart
    for card in cards:
        colors[card.color.value] += 1
        if colors[card.color.value] >= 5:
            dominant_color = card.color
            break

    # check if straight is in the dominant color
    # sort by rank, overrided operator < of c_card
    tmp = cards.copy()
    tmp.sort()
    # get last value -1 for first card to be counted as part of the sequence
    last_value = tmp[0].rank.value - 1
    straight = 0
    for card in tmp:
        # check if color is same
        if card.color == dominant_color:
            if card.rank.value == last_value + 1:
                straight += 1
                last_value = card.rank.value
            else:
                if straight >= 5:
                    return True
                # I broke the line, I have to start from this card
                straight = 1
                last_value = card.rank.value
    if straight >= 5:
        return True
    return False


def evaluate(cards):
    """evaluate set of cards"""
    result = [False, False, False, False, False, False, False, False]

    # first check for same ranks
    # check for a pair
    if check_pair(cards):
        result[e_evaluation.pair.value] = True
        # if there is a pair, delete it and check for another one
        a = delete_pair(cards)
        if check_pair(a):
            result[e_evaluation.two_pair.value] = True

        # if there is a pair, check for triple
        if check_triple(cards):
            result[e_evaluation.triple.value] = True
            # if there is a triple, delete it and check for full house
            a = delete_triple(cards)
            if check_pair(a):
                result[e_evaluation.full_house.value] = True

            # if there is a triple, check for quartet
            if checkquartet(cards)[0]:
                result[e_evaluation.quartet.value] = True
    if len(cards) != 7:
        raise ValueError("a")
    # check colors
    if checkflush(cards):
        result[e_evaluation.flush.value] = True

    # check straight
    if check_straight(cards):
        result[e_evaluation.straight.value] = True
        if result[e_evaluation.flush.value]:
            if check_straight_flush(cards):
                result[e_evaluation.straight_flush.value] = True

    return result


def decide_tie():
    """tie, make it random,
    it will statisticaly work,
    wont happen so often
    """
    if random.randint(0, 1) == 0:
        return True
    return False


def compare_higher_card(cards1, cards2):
    """
    compare sets of cards, where is no combination
    comparison is based on higher card
    returns true if first set is higher
    """
    cards1.sort()
    cards2.sort()
    for card1, card2 in zip(cards1, cards2):
        if card1.rank != card2.rank:
            if card1.rank.value > card2.rank.value:
                return True
            return False
    return decide_tie()


def compare_pairs(cards1, cards2):
    """
    compare sets of cards, where highest evaluation is pair
    returns true if first set is higher
    """
    first_val = check_pair(cards1)[1]
    second_val = check_pair(cards2)[1]
    if first_val != second_val:
        if first_val.value > second_val.value:
            return True
        return False
    return decide_tie()


def compare_triples(cards1, cards2):
    """
    compare sets of cards, where highest evaluation is triple
    returns true if first set is higher
    """
    first_val = check_triple(cards1)[1]
    second_val = check_triple(cards2)[1]
    if first_val != second_val:
        if first_val.value > second_val.value:
            return True
        return False
    return decide_tie()


def compare_quartet(cards1, cards2):
    """
    compare sets of cards, where highest evaluation is quartet
    returns true if first set is higher
    """
    first_val = checkquartet(cards1)[1]
    second_val = checkquartet(cards2)[1]
    if first_val != second_val:
        if first_val.value > second_val.value:
            return True
        return False
    return decide_tie()


def compare_two_pair(cards1, cards2):
    """
    compare sets of cards, where highest evaluation is two pair
    returns true if first set is higher
    """
    # sort list, we want higher cards to be first pair, that algorithm finds
    cards1.sort(reverse=True)
    cards2.sort(reverse=True)
    first_val = check_pair(cards1)[1]
    second_val = check_pair(cards2)[1]
    if first_val != second_val:
        if first_val.value > second_val.value:
            return True
        return False
    return decide_tie()


def compare_full_house(cards1, cards2):
    """
    compare sets of cards, where highest evaluation is full house
    returns true if first set is higher
    """
    # sort list, we want higher cards to be first pair, that algorithm finds
    cards1.sort(reverse=True)
    cards2.sort(reverse=True)
    first_val = check_pair(cards1)[1]
    second_val = check_pair(cards2)[1]
    if first_val != second_val:
        if first_val.value > second_val.value:
            return True
        return False
    return decide_tie()


def compare_flush(cards1, cards2):
    """
    compare sets of cards, where highest evaluation is flush
    returns true if first set is higher
    """
    first_val = find_highest_in_color(cards1)
    second_val = find_highest_in_color(cards2)
    if first_val != second_val:
        if first_val.value > second_val.value:
            return True
        return False
    return decide_tie()


def compare_straight_or_straight_flush(cards1, cards2):
    """
    compare sets of cards, where highest evaluation is straight or straight flush
    returns true if first set is higher
    """
    # sort list, we want higher cards to be first pair, that algorithm finds
    first_val = check_straight(cards1)[1]
    second_val = check_straight(cards2)[1]
    if first_val != second_val:
        if first_val.value > second_val.value:
            return True
        return False
    return decide_tie()


def compare_same_comb(cards1, cards2, highest_evaluation):
    """compare sets of cards, where highest combination is the same"""
    functions = [compare_pairs,
                 compare_two_pair,
                 compare_triples,
                 compare_straight_or_straight_flush,
                 compare_flush,
                 compare_full_house,
                 compare_quartet,
                 compare_straight_or_straight_flush]
    return functions[highest_evaluation.value](cards1, cards2)


def first_set_higher(cards1, cards2, evaluated1, evaluated2):
    """returns true if first is higher"""
    highest_evaluation = None
    for evaluation in reversed(e_evaluation):
        if evaluated1[evaluation.value] and evaluated2[evaluation.value]:
            highest_evaluation = evaluation
            return compare_same_comb(cards1, cards2, highest_evaluation)
        if evaluated1[evaluation.value] and not evaluated2[evaluation.value]:
            return True
        if not evaluated1[evaluation.value] and evaluated2[evaluation.value]:
            return False
    # no combination, compare higher card
    return compare_higher_card(cards1, cards2)
