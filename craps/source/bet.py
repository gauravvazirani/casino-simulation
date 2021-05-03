class Bet():

    def __init__(self, amount, outcome):
        self.amount = amount
        self.outcome = outcome
            
    def setOutcome(self, outcome):
        """
        Sets the Outcome for this bet. 
        This has the effect of moving the bet to another Outcome.
        """
        self.outcome = outcome

    def price(self):
        """
        Computes the price for this bet. 
        For most bets, the price is the amount. 
        Subclasses can override this to handle special cases.
        """
        pass 

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
    

class ComissionBet(Bet):
    def __init__(self, amount, outcome):
        super.__init__(amount, outcome)
        self.vig = 0.05

    def price(self):
        return self.amount + min(
            self.outcome.odds.numerator, 
            self.outcome.odds.denominator
        )
