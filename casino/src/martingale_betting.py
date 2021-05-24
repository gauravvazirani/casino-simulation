from . import betting_strategy
from . import outcome
from . import bet

class MartingaleBetting(betting_strategy.BettingStrategy):

    def __init__(self, outcome):
        super().__init__(outcome, 10) 
        self.loss_count = 0

    def createBet(self, player):
        bet_multiple = 2 ** self.loss_count
        return bet.Bet(
            self.bet_amount * bet_multiple, self.outcome, player)

    def win(self):
        self.loss_count = 0

    def lose(self):
        self.loss_count += 1
