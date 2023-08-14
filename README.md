# Poker AI
This Poker AI program is a player in the game of Texas Hold'em Poker. It calculates probabilities of various combinations based on available information (cards in hand and on the table), this information must be provided to the program, so the program is more like an assistant than a standalone player.

Starting from the three dealt cards, it simulates all possible potential combinations it could get and simulates all possible combinations for the opponent as well. It then compares all these combinations, calculates the probability of winning, and makes betting decisions based on that probability.

Everything is optimized to provide results within a reasonable time frame (competitive with a human opponent).

## Sub-problems:
- Evaluating a hand:
  - The AI needs to categorize a set of seven cards into combinations it can form. For example, full house, flush, straight. It can compare two sets of cards and determine which one is stronger.

- Probability calculations:
  - The AI computes all possible combinations beyond the three revealed cards. Calculates the probabilities of occurrence for different hand rankings (e.g., full house, flush) for both the AI and the opponent. Calculates the overall probability of winning.

- Betting strategy:
  - The AI manages its capital based on the calculated probabilities and makes appropriate bets or folds. The AI bets within its capital limits, possibly going all-in and following basic betting rules.

- User Interface (UI):
  - This computational model includes a simple text-based UI, which validates input correctness (e.g., entering the same card multiple times, incorrect card names, putting the same card in hand and on the table, etc.) and displays well-organized, color-coded tables with probabilities.

## Implementation

### Probabilities calculation
Challenges in solving the task were not so much in calculating probabilities themselves. This part involves straightforward programming, with the outcome already known. The approach to reach the solution isn't very complex or creative.

#### Number of players
First, it was important to address how to handle the number of players in each round. The number of players in a round doesn't affect the probability of winning, as the AI only sees its own cards and assumes the cards of the "strongest opponent." In other words, it doesn't matter to the AI which opponent defeats it, as this doesn't change the probability of winning. While information about the number of opponents could be relevant for a betting strategy, (e.g., if both opponents are raising bets but only one of them might have a good hand, the other might be bluffing), it's more of an advanced strategy. For the scope of this project, this information is not used extensively.

#### Ties
Next, in the probability calculation section, I tackled the issue of tied outcomes during simulated combinations. For example, both players have the same rank of three of a kind but different suits. In real games, this situation is resolved by splitting the pot. However, this approach isn't ideal for translating the simulation into numerical form for calculating probabilities. I devised a simple and effective solution to handle tied outcomes without significantly impacting the program's accuracy or performance. In tied situations, the program randomly selects a winner from a uniform distribution. Statistically, this approach will lead to outcomes converging to a 50:50 ratio with an increasing number of combinations. Such situations are infrequent enough that they don't significantly affect the overall results.

### Betting strategy
The betting strategy was a more complex challenge. It required determining reasonable bet amounts based on the calculated win probability. The process isn't as straightforward and deterministic as in probability calculations. For human play, it involves a lot of intuition. Hence, I devised several heuristics to simulate this intuition.

The program needs to compute two betting thresholds: An upper threshold for how much the program is willing to sacrifice when required. A natural bet amount the program would offer if it were the sole decision-maker.

First, I needed to decide which variables would determine these parameters.

The most crucial variable is the win probability. However, the win probability alone isn't enough to determine the bet amount, or at least not optimally. Consider a situation where the program has been betting a large number of chips, say 100, for a long time. Suddenly, its win probability drops from 60% to 20%, and the opponent demands an additional 5-chip bet from the program in the final round. A human might still contribute chips in this situation, as the ratio of potentially losing 5 chips against a chance to gain a much larger amount still favors betting. Therefore, another parameter affecting the betting process is the amount of money invested in the round so far, which increases both as the round progresses (more cards are revealed) and as the program keeps investing within a single round.

#### Game modes
Another parameter affecting the betting heuristic is the degree of uncertainty introduced by the program across three modes. The uncertainty, in this context, represents the correlation between strong hand and highness of bets.

- Low uncertainty: The program manages its resources well and maximizes gains when there's a high chance of winning, avoiding risks when the chance is low. This approach seems optimal but has a catch. Opponents can relatively easily read the program and anticipate its actions based on its bets. For example, if the program bets high, opponents might deduce that it has a strong hand, while low bets could indicate a weak hand, possibly leading the opponent to force the program to fold.

- High uncertainty: While opponents have less information about the program's cards, the program doesn't optimize its resource usage. It might not capitalize on situations where it has a high chance of winning and could attempt to bluff even when its chances are slim. This approach doesn't maximize gains.

- Moderate uncertainty: A compromise between the two approaches that balance gain maximization and resource management. These approaches were implemented using normal distributions and fine-tuned based on played games. For more details on the betting heuristic, refer to the [bets module](src/bets.py).

## Conclusion
The performance of the program is challenging to measure as there is no established automated way to gauge the performance of a poker AI. Although players can be ranked based on skill in poker, compared to games like chess where the Elo rating system is applicable, skill evaluation in poker is complex. Despite only a small number of games (approximately 5) against novice opponents, the program performed well with optimal settings. It managed to win all games. While the sample size is small, it's satisfying to develop a program that can outperform me in a certain aspect.

Although computers might not dominate in poker as they do in some other areas due to the game's semi-random nature and partially hidden information, having a program that is competitive with beginners and performs well against them can be considered a success. To further improve the program's performance, exploring machine learning could be beneficial, especially for enhancing the betting strategy. Possible avenues in machine learning include supervised learning, where the model learns from games of experts, or more advanced methods like reinforcement learning, where the model improves through self-play.

## How to run

how to run the application: python main.py PRUDENCE PREDICTABILITY
- PRUDENCE - how high amount is the agent willing to bet
  - options: conservative, optimal, risky

- PREDICTABILITY - how strong a correlation is there between cards and bets
  - options: low, optimal, high

The program should be simple to use.

Use the help in case of any trouble

Or run [the prepared script](run.sh).

### PyPy speedup
All code is only native Python without external libraries. So it is possible to run with [the PyPy compiler](https://www.pypy.org/) to save some execution time.

### Testes
The pytest command from the root directory.


## Author
- Name: Jakub Zeman
- GitHub: https://github.com/kzeman10
