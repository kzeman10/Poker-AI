"""module for testing bets.py"""
import pytest
import bets
import hyperparameters
import exceptions


# mocking default input of card module
def bet_generator(list_of_bets):
    """gerator returns bet from list"""
    for bet in list_of_bets:
        yield bet


def test_no_fold():
    """test that program will make bet, if it has high probability of winning"""
    # mock input
    bets_list = ['0', '0', '0']
    gen = bet_generator(bets_list)
    bets.input = lambda x: next(gen)
    bet = bets.make_bet(100, 150, hyperparameters.PRUDENCE['conservative'], hyperparameters.PREDICTABILITY['optimal'])
    assert bet > 10


def test_fold():
    """test that program will fold, if it has low probability of winning"""
    # mock input
    bets_list = ['200', '0', '0']
    gen = bet_generator(bets_list)
    bets.input = lambda x: next(gen)
    with pytest.raises(exceptions.fold):
        bets.make_bet(100, 150, hyperparameters.PRUDENCE['optimal'], hyperparameters.PREDICTABILITY['optimal'])
