import betting_strategy
import bet

class NoChangeBetting(betting_strategy):

    def __init__(self, outcome):
        super().outcome = outcome 

    def createBet(self, player):
        return bet.Bet(self.bet_amount, self.outcome, player)

    def win(self):
        pass

    def lose(self):
        pass


