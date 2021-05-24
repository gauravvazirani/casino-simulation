from . import betting_strategy
from . import bet

class NoChangeBetting(betting_strategy.BettingStrategy):

    def __init__(self, outcome):
        super().__init__(outcome, 10)
        # self.outcome = outcome
        # self.bet_amount = bet_amount

    def createBet(self, player):
        return bet.Bet(self.bet_amount, self.outcome, player)

    def win(self):
        pass

    def lose(self):
        pass
