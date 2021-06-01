from . import invalid_bet_exception
from .config import TABLE_MAXIMUM as MAX
from .config import TABLE_MINIMUM as MIN

class Table():
    """
    Table is responsible for holding a list of bets made by the player.
    A Table has a minimum and maximum limit on sum total of amount which a player 
    can bet at a time.
    """

    def __init__(self, minimum=MIN, maximum=MAX):
        self.minimum = minimum
        self.maximum = maximum
        self.bets = []


    def allValid(self):
        """
        Validates the sum of all bets within the table limits. 
        Returns false if the minimum is not met or the maximum is exceeded.
        """
        sum_of_bets = sum([bet.amount for bet in self.bets])
        if self.bets and (sum_of_bets > self.maximum or sum_of_bets < self.minimum):
            print("Sum of bets:",sum_of_bets)
            print("Bets on the table", self.bets)
            raise invalid_bet_exception.InvalidBetException
          
    def placeBet(self, bet, game):
        """
        Player can call this method to place a bet on the Table.
        Multiple bets can be placed by calling multiple method multiple times. 
        """
        if game.isValid(bet.outcome):
            self.bets.append(bet)
        else:
            raise invalid_bet_exception.InvalidBetException
    
    def clear(self):
        """
        Clear the game table, Useful if game needs to restart.
        """
        self.bets = []

    def __iter__(self):
        """
        :return: an iterable of bets on the table.
        """
        return self.bets.__iter__()
