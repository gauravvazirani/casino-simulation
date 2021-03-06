from . import roulette_player
from . import bet
from .config import FIBONACCI_PREVIOUS, FIBONACCI_CURRENT

class RouletteFibonacci(roulette_player.RoulettePlayer):
    """
    PlayerFibonacci uses the Fibonacci betting system. 
    This player allocates their available budget into a sequence of bets 
    that have an accelerating potential gain.
    """

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.previous = FIBONACCI_PREVIOUS
        self.current = FIBONACCI_CURRENT

    def playing(self):
        """
        whether or not a player is ready to play the next round.
        """
        if self.current <= self.stake:
            return super().playing()
        else:
            return False

    def placeBets(self, game):
        """
        Places and even money bet based on amount as per fibonacci betting strategy.
        Deducts bet amount from player's stake.
        """
        _bet = bet.Bet(amount=self.current, 
            outcome=self.wheel.all_outcomes.get('Black'))  
        self.table.placeBet(_bet, game)
        self.stake -= self.current
        
    def win(self, bet):
        """
        resets current and previous to their initial values of 1 and 0
        
        :param bet: (Bet) winning bet
        """
        super().win(bet)
        self.previous, self.current = 0, 1

    def lose(self):
        """
        This will go “forwards” in the sequence. 
        It updates recent and previous as follows.
        """
        self.previous, self.current = self.current, self.current + self.previous

