"""module for testing cards.py"""
import random
import math
import pytest
import cards


# mocking default input of card module
# lambda returning random card from all cards in deck
def card_generator():
    """gerator returns card from list"""
    all_cards = ['spade 2', 'spade 3', 'spade 4', 'spade 5', 'spade 6',
                 'spade 7', 'spade 8', 'spade 9', 'spade 10', 'spade j',
                 'spade q', 'spade k', 'spade a', 'heart 2', 'heart 3',
                 'heart 4', 'heart 5', 'heart 6', 'heart 7', 'heart 8',
                 'heart 9', 'heart 10', 'heart j', 'heart q', 'heart k',
                 'heart a', 'diamond 2', 'diamond 3', 'diamond 4', 'diamond 5',
                 'diamond 6', 'diamond 7', 'diamond 8', 'diamond 9', 'diamond 10',
                 'diamond j', 'diamond q', 'diamond k', 'diamond a', 'club 2',
                 'club 3', 'club 4', 'club 5', 'club 6', 'club 7', 'club 8',
                 'club 9', 'club 10', 'club j', 'club q', 'club k', 'club a']
    while True:
        card = random.choice(all_cards)
        all_cards.remove(card)
        yield card


def mock_input():
    """mock input"""
    gen = card_generator()
    cards.input = lambda x: next(gen)


def test_get_comb_from_deck_for_ValueError():
    """test get_comb_from_deck"""
    mock_input()
    card_sets = cards.c_card_sets()
    with pytest.raises(ValueError):
        card_sets.get_comb_from_deck(5)
    with pytest.raises(ValueError):
        card_sets.get_comb_from_deck('abc')
    with pytest.raises(ValueError):
        card_sets.get_comb_from_deck(-1)


# second phase of the game
def test_get_comb_from_deck4_oponent():
    """test get_comb_from_deck"""
    mock_input()
    card_sets = cards.c_card_sets()
    card_sets.table_next_stage()
    assert len(card_sets.get_comb_from_deck(4)) == math.comb(47, 4)


def test_get_comb_from_deck2_me():
    """test get_comb_from_deck"""
    mock_input()
    card_sets = cards.c_card_sets()
    card_sets.table_next_stage()
    assert len(card_sets.get_comb_from_deck(2)) == math.comb(47, 2)


# fifth phase of game
def test_get_comb_from_deck3_oponent():
    """test get_comb_from_deck"""
    mock_input()
    card_sets = cards.c_card_sets()
    card_sets.table_next_stage()
    card_sets.table_next_stage()
    assert len(card_sets.get_comb_from_deck(3)) == math.comb(46, 3)


def test_get_comb_from_deck1_me():
    """test get_comb_from_deck"""
    mock_input()
    card_sets = cards.c_card_sets()
    card_sets.table_next_stage()
    card_sets.table_next_stage()
    assert len(card_sets.get_comb_from_deck(1)) == math.comb(46, 1)


# fourth phase of game
def test_get_comb_from_deck2_oponent():
    """test get_comb_from_deck"""
    mock_input()
    card_sets = cards.c_card_sets()
    card_sets.table_next_stage()
    card_sets.table_next_stage()
    card_sets.table_next_stage()
    assert len(card_sets.get_comb_from_deck(2)) == math.comb(45, 2)


def test_get_comb_from_deck0_me():
    """test get_comb_from_deck"""
    mock_input()
    card_sets = cards.c_card_sets()
    print(len(card_sets.table))
    card_sets.table_next_stage()
    card_sets.table_next_stage()
    card_sets.table_next_stage()
    assert len(card_sets.get_comb_from_deck(0)) == math.comb(45, 0)
