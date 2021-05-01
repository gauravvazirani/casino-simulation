import player
import bet

class Fibonacci(player.IPlayer):
    """
    PlayerFibonacci uses the Fibonacci betting system. 
    This player allocates their available budget into a sequence of bets 
    that have an accelerating potential gain.
    """

    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table
        self.stake = 1000
        self.outcome = self.wheel.all_outcomes.get('Black')
        self.previous = 0
        self.current = 1

    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if self.rounds_to_go > 0 and self.current <= self.stake \
              else False

    def placeBets(self):
        _bet = bet.Bet(amount=self.current, outcome=self.outcome)  
        self.table.placeBet(_bet)
        self.stake -= self.current
        
    def win(self, bet):
        """
        resets current and previous to their initial values of 1 and 0
        """
        self.stake += bet.winAmount()
        self.previous, self.current = 0, 1

    def lose(self, bet):
        """
        This will go “forwards” in the sequence. 
        It updates recent and previous as follows.
        """
        self.previous, self.current = self.current, self.current + self.previous

    def winners(self, winning_outcomes):
        pass
