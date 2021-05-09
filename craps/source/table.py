import os
import invalid_bet_exception

class Table():
    """
    Table is responsible for holding a list of bets made by the player.
    A Table has a limit on sum total of amount upto which a player 
    can bet at a time.
    """

    def __init__(self, limit=1000):
        self.bets = []
        self.limit = limit

    def placeBet(self, bet):
        """
        Player can call this method to place a bet on the Table.
        Multiple bets can be placed by calling multiple method multiple times. 
        """
        self.bets.append(bet)

    def __str__(self):
        """
        Return an easy-to-read string representation of all current bets.
        """
        return f"Bets Currently on table:{os.linesep}{os.linesep.join([str(bet) for bet in self.bets])}"

    def __repr__(self):
        """
        Return a representation of the form Table( bet, bet, ... ).
        """
        return f"Table({','.join([bet.__repr__() for bet in self.bets])})"

    def __iter__(self):
        """
        :returns: an iterator over the bet instances
        """
        return self.bets.__iter__()
        
    def allValid(self):
        """
        Raises a invalide bet exception if the following conditions are not met:
        1.The sum of all bets is less than or equal to the table limit.
        """
        if sum([bet.amount for bet in self.bets]) > self.limit:
            raise invalid_bet_exception.InvalidBetException
    
    def clear(self):
        """
        Clear all the bets currently on the table
        """
        self.bets = []
    
class  CrapsTable(Table):

    def __init__(self, game, limit=1000):
      super().__init__(limit)
      self.game = game

    def isValid(self, bet):
        """
        Validates this bet by checking with the CrapsGame to see if the bet is valid; 
        it returns true if the bet is valid, false otherwise.
        """
        return self.game.isAllowed(bet.outcome)
    
    def allValid(self):
        """
        This uses the superclass to see if the sum of all bets is less than 
        or equal to the table limit. 
        If the individual bet outcomes are also valid, return true. 
        Otherwise, return false.
        """
        super().allValid()
        for bet in self.bets:
            if not self.isValid(bet):
                return False
        return True
