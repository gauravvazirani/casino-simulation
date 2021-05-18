import betting_strategy
import outcome
import bet

class MartingaleBetting(betting_strategy):

    def __init__(self):
        super().outcome = outcome.Outcome(
            'Pass Line', 1) 
        self.loss_count = 0

    def createBet(self, player):
        bet_multiple = 2 ** self.loss_count
        return bet.Bet(
            self.bet_amount * bet_multiple, self.outcome, player)

    def win(self):
        self.loss_count = 0

    def lose(self):
        self.loss_count += 1
