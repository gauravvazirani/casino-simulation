class Bet():

    def __init__(self, amount, outcome, player=None):
        self.amount = amount
        self.outcome = outcome
        self.player = player
            
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
        return self.amount 

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
    

class CommissionBet(Bet):
    def __init__(self, amount, outcome, player):
        super().__init__(amount, outcome, player)
        self.vig = 0.05

    def price(self):
        """ 
        There are two variations of commission bets : Buy bets and Lay bets.
        
        A Buy bet is a right bet; it has a numerator greater than or equal to the denominator, 
        the price is 5% of the amount bet. A $20 Buy bet has a price of $21.
        
        A Lay bet is a wrong bet; it has a denominator greater than the numerator, 
        the price is 5% of num/den of the amount. 
        A $30 bet Layed at 2:3 odds has a price of $31, 
        the $30 bet, plus the vig of 5% of $20 payout.
        """
        if self.outcome.odds.numerator >= self.outcome.odds.denominator:
            commission = self.vig * self.amount
        else:
            commission = (self.vig 
                        * self.amount 
                        * self.outcome.odds.numerator 
                        / self.outcome.odds.denominator)
        return self.amount + round(commission,2)                
        