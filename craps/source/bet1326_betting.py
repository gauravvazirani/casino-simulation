import betting_strategy
import outcome
import bet
import player1326_state

class craps1326Betting(betting_strategy):

    def __init__(self):
        super().outcome = outcome.Outcome(
            'Pass Line', 1) 
        self.loss_count = 0
        self.state = player1326_state.PlayerNoWins(
            self, 
            self.odds
            )

    def createBet(self, player):
        bet = bet.Bet(
            self.bet_amount, self.outcome, player)
        bet.player = player
        return bet

    def win(self):
        self.state = self.state.nextWon()

    def lose(self):
        self.state = self.state.nextLost()
