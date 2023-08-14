"""module for calculating probabilities"""
from evaluation import evaluate, e_evaluation, first_set_higher
import colors


def calculate_for_me(cards):
    """
    function computes probabilities of getting each combination
    """
    combs = cards.get_comb_from_deck(5 - len(cards.table))
    no_all_combs = len(combs)
    my_numbers_of_comb = [0, 0, 0, 0, 0, 0, 0, 0]
    my_probabilities = [0, 0, 0, 0, 0, 0, 0, 0]
    for comb in combs:
        all_comb = cards.hand + cards.table + comb
        evaluated = evaluate(all_comb)
        for evaluation in e_evaluation:
            if evaluated[evaluation.value]:
                my_numbers_of_comb[evaluation.value] += 1

    print("")
    print("\ntable of probabilities for me")
    for evaluation in e_evaluation:
        my_probabilities[evaluation.value] = my_numbers_of_comb[evaluation.value] / no_all_combs
        text1 = f"probability of {evaluation.name}:"
        print(text1, (30 - len(text1)) * " ",
              f"{(my_probabilities[evaluation.value] * 100):.2f} %".rjust(7, " "))
    return my_probabilities


def calculate_for_enemy(cards):
    """
    function computes probabilities of getting each combination
    """
    combs = cards.get_comb_from_deck(7 - len(cards.table))
    no_all_combs = len(combs)
    enemy_numbers_of_comb = [0, 0, 0, 0, 0, 0, 0, 0]
    enemy_probabilities = [0, 0, 0, 0, 0, 0, 0, 0]
    my_wins = 0
    last_comb = []
    for comb in combs:
        enemy_comb = cards.table + comb
        my_comb = cards.table + comb[: (5 - len(cards.table))] + cards.hand
        enemy_evaluated = evaluate(enemy_comb)
        if my_comb != last_comb:
            my_evaluated = evaluate(my_comb)
            last_comb = my_comb

        # comparing winning make optimizations
        if first_set_higher(my_comb, enemy_comb, my_evaluated, enemy_evaluated):
            my_wins += 1

        for evaluation in e_evaluation:
            if enemy_evaluated[evaluation.value]:
                enemy_numbers_of_comb[evaluation.value] += 1

    print("")
    print("\ntable of probabilities for enemy")
    for evaluation in e_evaluation:
        enemy_probabilities[evaluation.value] = enemy_numbers_of_comb[evaluation.value] / no_all_combs
        text1 = f"probability of {evaluation.name}:"
        print(text1, (30 - len(text1)) * " ",
              f"{(enemy_probabilities[evaluation.value] * 100):.2f} %".rjust(7, " "))
    return enemy_probabilities, no_all_combs, my_wins


def calculate(cards):
    """
    main computational function
    computes probabilities of all combination for me and for enemy
    and also probability of winning
    """
    my_probabilities = calculate_for_me(cards)
    enemy_probabilities, no_all_combs, my_wins = calculate_for_enemy(cards)

    # get combined score, difference between my probability and enemy probability for each given evaluation
    result_probabilities = [0, 0, 0, 0, 0, 0, 0, 0]
    for i, it in enumerate(zip(my_probabilities, enemy_probabilities)):
        result_probabilities[i] = it[0] - it[1]

    print("")
    print(colors.BLUE + "\ntable of combined probabilities for me in depence on enemy" + colors.NORMAL)
    for evaluation in e_evaluation:
        text1 = f"probability of {evaluation.name}:"
        if result_probabilities[evaluation.value] >= 0:
            color = colors.GREEN
        else:
            color = colors.RED
        print(text1, (30 - len(text1)) * " " + color + f"{(result_probabilities[evaluation.value] * 100):.2f}".rjust(7, " ") + colors.NORMAL + " %")

    # probability of winning
    my_wins_percents = (my_wins * 100) / no_all_combs
    if my_wins_percents >= 50:
        color = colors.GREEN
    else:
        color = colors.RED

    print("percent of my wins is:" + color,
          f"{my_wins_percents:.2f} %" + colors.NORMAL)
    return my_wins_percents
