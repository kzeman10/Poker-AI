"""module for testing the evaluation module"""
from cards import c_card, e_color, e_rank
from evaluation import check_pair, evaluate, first_set_higher


def test_check_pair():
    """test the check_pair function"""
    cards = [c_card(e_color.club, e_rank.two),
             c_card(e_color.spade, e_rank.two),
             c_card(e_color.club, e_rank.four),
             c_card(e_color.club, e_rank.three),
             c_card(e_color.club, e_rank.six),
             c_card(e_color.heart, e_rank.three),
             c_card(e_color.club, e_rank.five)]
    assert check_pair(cards)


def test_evaluate():
    """test the evaluate function"""
    cards = [c_card(e_color.club, e_rank.two),
             c_card(e_color.spade, e_rank.two),
             c_card(e_color.club, e_rank.four),
             c_card(e_color.club, e_rank.three),
             c_card(e_color.club, e_rank.six),
             c_card(e_color.heart, e_rank.three),
             c_card(e_color.club, e_rank.five)]
    assert evaluate(cards) == [True, True, False, True, True, False, False, True]
    # [pair, two_pair, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush]


def test_evaluate2():
    """test the evaluate function"""
    cards = [c_card(e_color.club, e_rank.ten),
             c_card(e_color.club, e_rank.j),
             c_card(e_color.club, e_rank.q),
             c_card(e_color.club, e_rank.k),
             c_card(e_color.club, e_rank.a),
             c_card(e_color.heart, e_rank.three),
             c_card(e_color.club, e_rank.five)]
    # [pair, two_pair, three_of_a_kind, straight, flush, full_house, four_of_a_kind, straight_flush]
    assert evaluate(cards) == [False, False, False, True, True, False, False, True]


def test_first_set_higher():
    """test the first_set_higher function"""
    cards1 = [c_card(e_color.club, e_rank.two),
              c_card(e_color.spade, e_rank.two),
              c_card(e_color.club, e_rank.four),
              c_card(e_color.club, e_rank.three),
              c_card(e_color.club, e_rank.six),
              c_card(e_color.heart, e_rank.three),
              c_card(e_color.club, e_rank.five)]

    cards2 = [c_card(e_color.diamond, e_rank.a),
              c_card(e_color.spade, e_rank.two),
              c_card(e_color.club, e_rank.nine),
              c_card(e_color.heart, e_rank.j),
              c_card(e_color.club, e_rank.six),
              c_card(e_color.heart, e_rank.three),
              c_card(e_color.club, e_rank.five)]
    assert first_set_higher(cards1, cards2, evaluate(cards1), evaluate(cards2))
