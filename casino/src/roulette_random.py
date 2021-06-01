from . import roulette_player
import random
from . import bet 
from .config import RANDOM_BET_AMOUNT as BET_AMOUNT

class RouletteRandom(roulette_player.RoulettePlayer):
    """
    Chooses a random outcome and bets base amount on it.
    """

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.rng = random.Random()
        self.outcomes = tuple(outcome_obj for bin_obj in self.wheel for outcome_obj in bin_obj)
        self.bet_amount = BET_AMOUNT

    def placeBets(self, game):
        """
        Places a bet on a random outcome.
        adjusts player stake for making the bet.
        """
        random_outcome = self.outcomes[self.rng.randint(0, len(self.outcomes)-1)]
        self.table.placeBet(bet.Bet(self.bet_amount ,random_outcome), game)
        self.stake -= self.bet_amount
        