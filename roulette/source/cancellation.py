import player
import bet

class Cancellation(player.IPlayer):
    """
    PlayerCancellation uses the cancellation betting system. 
    This player allocates their available budget into a sequence of bets 
    that have an accelerating potential gain as well as recouping any losses.
    """
    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table
        self.stake = 1000
        self.sequence = self.resetSequence()
        self.outcome = self.wheel.all_outcomes.get('Black')
        if len(self.sequence)==1:
            self.bet_amount = self.sequence[0]
        elif len(self.sequence)>1:
            self.bet_amount = self.sequence[0] + self.sequence[-1] 

    def resetSequence(self):
        """
        Puts the initial sequence of six Integer instances into 
        the sequence variable. 
        These Integers are built from the values 1 through 6.
        """
        return [num for num in range(1,7)]

    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if self.rounds_to_go > 0 and self.sequence \
            and self.bet_amount <= self.stake \
              else False

    def placeBets(self):
        """
        Creates a bet from the sum of the first and last values of sequence 
        and the preferred outcome.
        """
        _bet = bet.Bet(amount=self.bet_amount, outcome=self.outcome)  
        self.table.placeBet(_bet)
        self.stake -= self.bet_amount
        
    def win(self, bet):
        """
        Uses the superclass method to update the stake with an amount won.
        It then removes the fist and last element from sequence.
        """
        self.stake += bet.winAmount()
        del self.sequence[0]
        if self.sequence:
            del self.sequence[-1]
        self.update_amount()

    def lose(self, bet):
        """
        Uses the superclass method to update the stake with an amount lost. 
        It then appends the sum of the first and list elements of sequence 
        to the end of sequence as a new Integer value.
        """
        self.sequence.append(self.sequence[0]+self.sequence[-1])
        self.update_amount()

    def update_amount(self):
        """
        Calculates the bet amount from the sequence of values
        """
        if len(self.sequence)==1:
            self.bet_amount = self.sequence[0]
        elif len(self.sequence)>1:
            self.bet_amount = self.sequence[0] + self.sequence[-1] 

    def winners(self, winning_outcomes):
        pass
