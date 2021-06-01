from . import roulette_player
from . import bet
from .config import MARTINGALE_BET_AMOUNT as BET_AMOUNT

class RouletteMartingale(roulette_player.RoulettePlayer):
    """
    Roulette player which follows martingale strategy.   
    Tries to make up for a loss by doubling the bet amount.
    """

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.initial_bet_amount = BET_AMOUNT
        self.loss_count = 0
              
    def placeBets(self, game):
        """
        Calculates the bet multiplier based on the number of consecutive loses encountered.
        Places an even money bet on the table.
        Deducts Bet amount from player balance.
        """
        bet_multiple = 2**self.loss_count
        bet_amount = self.initial_bet_amount * bet_multiple
        black = self.wheel.all_outcomes.get('Black')
        self.table.placeBet(bet.Bet(bet_amount ,black), game)
        self.stake -= bet_amount
    
    def win(self, bet):
        """
        Resets loss count back to initial state of 0.
        Leaves the stake adjustment to the super class.
        """
        super().win(bet)
        self.loss_count = 0 

    def lose(self):
        """
        Increments loss count by 1.
        Leaves the stake adjustment to the super class.
        """
        self.loss_count += 1
