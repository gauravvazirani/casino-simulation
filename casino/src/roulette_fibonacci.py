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
        """
        whether or not a player is ready to play the next round.
        """
        if self.current <= self.stake:
            return super().playing()
        else:
            return False

    def placeBets(self):
        """
        Places and even money bet based on amount as per fibonacci betting strategy.
        Deducts bet amount from player's stake.
        """
        _bet = bet.Bet(amount=self.current, 
            outcome=self.wheel.all_outcomes.get('Black'))  
        self.table.placeBet(_bet)
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

