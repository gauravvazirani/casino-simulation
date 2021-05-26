from . import betting_strategy
from . import player1326_state

class Craps1326Betting(betting_strategy.BettingStrategy):
    """
    Strategy that changes a bet multiplier on winning.
    Current bet amount is multiplier times current bet amount.
    The strategy follows the pattern 1-3-2-6.
    On losing, the pattern resets to 1.
    """

    def __init__(self, outcome):
        super().__init__(outcome, 10)  
        self.initial_bet_amount = self.bet_amount
        self.state = player1326_state.PlayerNoWins(
            self, 
            outcome
            )

    def createBet(self, player):
        """
        :return: (Bet) bet constructed based on current state of the game. 
        """
        _bet = self.state.currentBet()
        _bet.player = player
        return _bet

    def win(self):
        """
        calls the nextWon() method of the state class to change the current state 
        of the game.
        """
        self.state = self.state.nextWon()

    def lose(self):
        """
        calls the nextLost() method of the state class to change the current state 
        of the game.
        """
        self.state = self.state.nextLost()
