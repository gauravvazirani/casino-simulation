from . import betting_strategy
from . import bet
from .config import NOCHANGE_BETTING_AMOUNT as BET_AMOUNT

class NoChangeBetting(betting_strategy.BettingStrategy):
    """
    Betting strategy which repeatedly makes the same bets without change. 
    """
    
    def __init__(self, outcome):
        super().__init__(outcome, BET_AMOUNT)

    def createBet(self, player):
        """
        returns a bet after assigning a player to it.

        :return: (Bet) 
        """
        return bet.Bet(self.bet_amount, self.outcome, player)

    def win(self):
        """
        makes no change to the betting style
        """
        pass

    def lose(self):
        """
        makes no change to the betting style
        """
        pass
