class Bet():
    """
    A Bet is an Amount wagered on an Outcome.
    A Player has to make atleast one Bet to play a
    Game. 
    """

    def __init__(self, amount, outcome):
        self.amount = amount
        self.outcome = outcome
    
    def winAmount(self):
        """
        Calculates the Amount won in a bet 
        in case the Outcome of the Game is favourable.
        """
        return self.outcome.winAmount(self.amount) + self.amount

    def loseAmount(self):
        """
        Calculates the Amount lost in a bet.
        """
        return self.amount
    
    def __str__(self):
        """
        Returns a minimal description of the Bet made.
        """
        return f"{self.amount} on {self.outcome.name}"
    
    def __repr__(self):
        """
        Returns the string representation of the Bet.
        """
        return f"Bet({self.amount}, {self.outcome.name})"
    