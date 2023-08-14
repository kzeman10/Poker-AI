"""module for making bets"""
from math import ceil
import random
import colors
from calculations import calculate
from evaluation import check_pair
from exceptions import fold, all_in


def make_first_matg(money, cards):
    """
    for special situations, when I have only a little money
    to not be afraid to go to the all in
    """
    money += 10
    # batg = beiing able to give in percent
    batg = 0.01
    if check_pair(cards.hand):
        batg += 0.02
    for card in cards.hand:
        if card.rank.value > 10:
            batg += 0.03

    # matg = money beiing able to give
    matg = ceil(money * batg)
    return matg


def make_matg(money, old_bets, cards):
    """
    amplified matg
    when low chance I do not want to spend so much
    if I have high chance, I can spend safely
    1/5 of old bets included, when I already ivested into this round, I do not want to lost it
    and I want to look confident
    """
    win_chance = calculate(cards)
    matg = ceil(money * (win_chance / 100)**4 + old_bets / 5)
    return matg


def make_bet(matg, money, prudence, predictability):
    """
    create natural bet based on maximum amount of money, that I am able to invest
    """
    mean = ceil(prudence * matg)
    var = ceil(matg / predictability)
    natural_bet = round(random.gauss(mean, var))

    ans = ""
    bet = 0
    ammount_to_call = 0
    print(colors.BLUE + "Now it is time for betting", colors.NORMAL)
    print(colors.BLUE + "your money left:", money, colors.NORMAL)
    print("type type ok when betting is done or")
    print("type end if round is done")

    for _ in range(2):
        # this is only ammount, that i should add
        # if I already gave something, I will only add the rest
        ans = input(colors.RED + "ammount to add: " + colors.NORMAL).lower()

        while not ans.isnumeric():
            if ans == "end":
                raise fold("end of the round, others probably fold")
            if ans == "ok":
                return bet
            print("bet should be positive integer")
            ans = input(colors.RED + "ammount to add: " + colors.NORMAL).lower()

        ammount_to_call = int(ans)
        if ammount_to_call < natural_bet:
            bet += natural_bet
            if money - natural_bet > 0:
                print("raise:", natural_bet)
            else:
                print("all in")
                raise all_in("no betting needed")
        elif ammount_to_call <= matg:
            bet += ammount_to_call
            if money - natural_bet > 0:
                print("call")
            else:
                print("all in")
                raise all_in("no betting needed")
        else:
            print("fold")
            raise fold("fold")

        # increase ammount of money, I am willing to give
        # because I have already invested more into this round
        # so I do not want to lost it
        matg += ceil(bet * 0.3)
        # and remove from it money, that I have already gave
        matg -= bet

        # now I have to just check, what others raised or fold
        # I do not have right to raise bet anymore
        natural_bet = 0

    if ans == "end":
        raise fold("end of the round, others probably fold")
    return bet
