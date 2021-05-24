from . import roulette_player
from . import bet

class RouletteFibonacci(roulette_player.RoulettePlayer):
    """
    PlayerFibonacci uses the Fibonacci betting system. 
    This player allocates their available budget into a sequence of bets 
    that have an accelerating potential gain.
    """

    def __init__(self, wheel, table):
        super().__init__(table, wheel)
        self.previous = 0
        self.current = 1

    def playing(self):
        if self.current <= self.stake:
            return super().playing()
        else:
            return False

    def placeBets(self):
        _bet = bet.Bet(amount=self.current, 
            outcome=self.wheel.all_outcomes.get('Black'))  
        self.table.placeBet(_bet)
        self.stake -= self.current
        
    def win(self, bet):
        """
        resets current and previous to their initial values of 1 and 0
        """
        super().win(bet)
        self.previous, self.current = 0, 1

    def lose(self):
        """
        This will go “forwards” in the sequence. 
        It updates recent and previous as follows.
        """
        self.previous, self.current = self.current, self.current + self.previous

