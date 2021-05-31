from . import roulette_player
import random
from . import bet 

class RouletteRandom(roulette_player.RoulettePlayer):
    """
    Chooses a random outcome and bets base amount on it.
    """

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.rounds_to_go = 250
        self.rng = random.Random()
        self.outcomes = tuple(outcome_obj for bin_obj in self.wheel for outcome_obj in bin_obj)

    def placeBets(self, game):
        """
        Places a bet on a random outcome.
        adjusts player stake for making the bet.
        """
        bet_amount = 10
        random_outcome = self.outcomes[self.rng.randint(0, len(self.outcomes)-1)]
        self.table.placeBet(bet.Bet(bet_amount ,random_outcome), game)
        self.stake -= bet_amount
        