"""this module operates the game"""
from cards import c_card_sets
from bets import make_bet, make_matg, make_first_matg
from exceptions import fold, all_in


def game(money, prudence, predictability):
    """
    main function, operates the game
    """
    bet = 0

    # get cards to the hand
    cards = c_card_sets()

    # make first bet based on heuristic with cards in the hand
    # no complicated computations
    try:
        current_bet = make_bet(make_first_matg(money, cards), money, prudence, predictability)
        money -= current_bet
        bet += current_bet
    except (fold, all_in):
        return

    # reveal 3 cards and make bet based on computations and betting heuristic
    cards.table_next_stage()
    try:
        current_bet = make_bet(make_matg(money, bet, cards), money, prudence, predictability)
        money -= current_bet
        bet += current_bet
    except (fold, all_in):
        return

    # reveal 1 card and make bet based on computations and betting heuristic
    cards.table_next_stage()
    try:
        current_bet = make_bet(make_matg(money, bet, cards), money, prudence, predictability)
        money -= current_bet
        bet += current_bet
    except (fold, all_in):
        return

    # reveal 1 card and make bet based on computations and betting heuristic
    cards.table_next_stage()
    try:
        current_bet = make_bet(make_matg(money, bet, cards), money, prudence, predictability)
        money -= current_bet
        bet += current_bet
    except (fold, all_in):
        return
    print("total bet for this game is:", bet)
