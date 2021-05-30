from . import invalid_bet_exception

class Table():
    """
    Table is responsible for holding a list of bets made by the player.
    A Table has a minimum and maximum limit on sum total of amount which a player 
    can bet at a time.
    """

    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum
        self.bets = []
        self.game = None

    def setGame(self, game):
        """
        Saves the given game to be used to validate bets
        """
        self.game = game

    def isValid(self, bet):
        """
        Validates this bet. 
        The first test, checks test to see if the bet is valid.
        """
        return self.game.isValid(bet.outcome) 

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
          
    def placeBet(self, bet):
        """
        Player can call this method to place a bet on the Table.
        Multiple bets can be placed by calling multiple method multiple times. 
        """
        if self.isValid(bet):
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
