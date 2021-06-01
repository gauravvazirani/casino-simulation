from . import bet
from . import roulette_player
from . import player1326_state
from .config import ROULETTE_1326_BET_AMOUNT as BET_AMOUNT

class Roulette1326(roulette_player.RoulettePlayer):
    """
    Player that changes the multiplier on winning.
    The strategy follows the pattern 1-3-2-6.
    On losing, the pattern resets.
    """

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.initial_bet_amount = BET_AMOUNT
        self.state = player1326_state.PlayerNoWins(
            self, 
            self.wheel.all_outcomes.get('Black')
            )

    def placeBets(self, game):
        """
        places a bet based on the current state of the game.
        i.e. number of wins and deducts the amount from the stake.
        """
        bet = self.state.currentBet()
        self.table.placeBet(bet, game)
        self.stake -= bet.amount
    
    def win(self, bet):
        """
        Calls the superclass method to perform monetary adjustment.
        Moves the current game to next appropriate state.

        :param bet: 
        """
        super().win(bet)
        self.state = self.state.nextWon()

    def lose(self):
        """
        Calls the superclass method to perform monetary adjustment.
        Moves the current game to next appropriate state.
        """
        self.state = self.state.nextLost()
