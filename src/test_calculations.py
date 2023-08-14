"""module for testing calculations.py"""
import cards
import calculations


# mocking default input of card module
def card_generator(list_of_cards):
    """gerator returns card from list"""
    for card in list_of_cards:
        yield card


def test_pair_prob():
    """test pair probability"""
    # mock input
    # I have two cards, that are not on the table, that has one last card hidden
    pair = ['spade 2', 'heart 3', 'diamond 4', 'club 6', 'club 7', 'spade 8']
    gen = card_generator(pair)
    cards.input = lambda x: next(gen)

    card_set = cards.c_card_sets()
    card_set.table_next_stage()
    card_set.table_next_stage()
    probability = calculations.calculate_for_me(card_set)[0]
    # ref probability - there are 6 * 8 cards that will give me pair and 52 - 6 cards left in deck
    ref_probability = (6 * 3) / (52 - 6)
    # check if probability is in range of 1% from reference
    assert ref_probability * 0.99 <= probability <= ref_probability * 1.01


def test_tripple_prob():
    """test tripple probability"""
    # mock input
    # I have two cards, that are not on the table, that has one last card hidden
    tripple = ['spade 2', 'heart 2', 'diamond 4', 'club 6', 'club 7', 'spade 8']
    gen = card_generator(tripple)
    cards.input = lambda x: next(gen)

    card_set = cards.c_card_sets()
    card_set.table_next_stage()
    card_set.table_next_stage()
    probability = calculations.calculate_for_me(card_set)[2]
    # ref probability - there are 2 cards that will give me tripple and 52 - 6 cards left in deck
    ref_probability = (2) / (52 - 6)
    # check if probability is in range of 1% from reference
    assert ref_probability * 0.99 <= probability <= ref_probability * 1.01


def test_full_house():
    """test full house"""
    # mock input
    # I have two cards, that are not on the table, that has one last card hidden
    full_house = ['spade 2', 'heart 2', 'diamond 6', 'club 4', 'diamond 4', 'spade 8']
    gen = card_generator(full_house)
    cards.input = lambda x: next(gen)

    card_set = cards.c_card_sets()
    card_set.table_next_stage()
    card_set.table_next_stage()
    probability = calculations.calculate_for_me(card_set)[5]
    # ref probability - there are 4 cards that will give me full house and 52 - 6 cards left in deck
    ref_probability = (4) / (52 - 6)
    # check if probability is in range of 1% from reference
    assert ref_probability * 0.99 <= probability <= ref_probability * 1.01


def test_clear_win():
    """test clear win"""
    # mock input
    straight_flush = ['spade 2', 'spade 3', 'spade 4', 'spade 5', 'spade 6', 'heart 2', 'heart 3']
    gen = card_generator(straight_flush)
    cards.input = lambda x: next(gen)

    card_set = cards.c_card_sets()
    card_set.table_next_stage()
    card_set.table_next_stage()
    card_set.table_next_stage()
    assert calculations.calculate(card_set) >= 99


def test_clear_loss():
    """test clear loss"""
    # mock input
    # low ranks, but different, different colors
    # this is the worst hand, probability of winning should be very low
    # only combination is high card, which is 9 and is on the table, so opoent has it too
    loosers_hand = ['spade 2', 'heart 3', 'diamond 4', 'club 6', 'club 7', 'spade 8', 'diamond 9']
    gen = card_generator(loosers_hand)
    cards.input = lambda x: next(gen)

    card_set = cards.c_card_sets()
    card_set.table_next_stage()
    card_set.table_next_stage()
    card_set.table_next_stage()
    assert calculations.calculate(card_set) <= 1
