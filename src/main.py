"""main module for running the program"""
import sys
import colors
from game import game
import hyperparameters

# checks if there are two arguments
if len(sys.argv) == 3:
    prudence = sys.argv[1]
    if prudence not in hyperparameters.PRUDENCE:
        print(f"{prudence} not in prudence hyperparameters")
        sys.exit(1)
    predictability = sys.argv[2]
    if predictability not in hyperparameters.PREDICTABILITY:
        print(f"{predictability} not in predictability hyperparameters")
        sys.exit(1)
else:
    print(len(sys.argv))
    print("usage: python main.py prudence predictability")
    print("example: python main.py optimal optimal")
    sys.exit(1)

print(colors.GREEN + "Welcome in poker asistant." + colors.NORMAL)
print(colors.BLUE + """
This program plays poker for you, but requires your assistance.
You will be asked to share information about cards in your hand and on the table.
You will be also asked to share information about bets.
Program suppose only one opoenent with strongest possible hand. But is able to play against multiple opponents.
""" + colors.NORMAL)

try:
    # cycle, each round ask for money
    while True:
        money = input(colors.GREEN + "your money for this round: " + colors.NORMAL)
        if money.isnumeric():
            money = int(money)
            break
        print(colors.RED + "enter positive integer!" + colors.NORMAL)

    print(colors.GREEN + "OK!" + colors.NORMAL)

    game(money, hyperparameters.PRUDENCE[prudence], hyperparameters.PREDICTABILITY[predictability])
except KeyboardInterrupt:
    print(colors.RED + "\nIinterrupted, program about to end" + colors.NORMAL)

print("program ends")
