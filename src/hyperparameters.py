"""constants for hyperparameters"""


# Prudence hyperparameters
# how high amount is agent willing to bet
PRUDENCE = {
    "conservative": 0.5,
    "optimal": 0.65,
    "risky": 0.8
}

# Predictability hyperparameters
# how strong corelation is there between cards and bets
PREDICTABILITY = {
    "low": 4,
    "optimal": 8,
    "high": 12
}
