import bet
import craps_player

class CrapsCancellation(craps_player.CrapsSimplePlayer):
    """
    PlayerCancellation uses the cancellation betting system. 
    This player allocates their available budget into a sequence of bets 
    that have an accelerating potential gain as well as recouping any losses.
    """
    def __init__(self, table, line, odds):
        super().__init__(table, line, odds)
        self.sequence = []
        self.resetSequence()

    def resetSequence(self):
        """
        Puts the initial sequence of six Integer instances into 
        the sequence variable. 
        These Integers are built from the values 1 through 6.
        """
        self.sequence = [num for num in range(1,7)]

    def playing(self):
        if self.sequence:
            return super().playing()
        else:
            return False

    def oddsBet(self):
        """
        Creates a bet from the sum of the first and last values of sequence 
        and the preferred outcome.
        """
        if len(self.sequence)==1:
            bet_amount = self.sequence[0]
        elif len(self.sequence)>1:
            bet_amount = self.sequence[0] + self.sequence[-1] 
        _bet = bet.Bet(amount=bet_amount, outcome=self.odds)  
        self.table.placeBet(_bet)
        self.stake -= bet_amount
        
    def win(self, bet):
        """
        Uses the superclass method to update the stake with an amount won.
        It then removes the fist and last element from sequence.
        """
        super().win(bet)
        del self.sequence[0]
        if self.sequence:
            del self.sequence[-1]


    def lose(self):
        """
        Uses the superclass method to update the stake with an amount lost. 
        It then appends the sum of the first and list elements of sequence 
        to the end of sequence as a new Integer value.
        """
        self.sequence.append(
            self.sequence[0]+self.sequence[-1])
