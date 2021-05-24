from . import betting_strategy
from . import player1326_state

class Craps1326Betting(betting_strategy.BettingStrategy):

    def __init__(self, outcome):
        super().__init__(outcome, 10)  
        self.initial_bet_amount = self.bet_amount
        self.state = player1326_state.PlayerNoWins(
            self, 
            outcome
            )

    def createBet(self, player):
        _bet = self.state.currentBet()
        _bet.player = player
        return _bet

    def win(self):
        self.state = self.state.nextWon()

    def lose(self):
        self.state = self.state.nextLost()
