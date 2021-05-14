import invalid_bet_exception

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
        return self.game.isValid(bet) 

    def allValid(self):
        """
        Validates the sum of all bets within the table limits. 
        Returns false if the minimum is not met or the maximum is exceeded.
        """
        sum_of_bets = sum([bet.amount for bet in self.bets])
        if sum_of_bets > self.maximum or sum_of_bets < self.minimum:
                raise invalid_bet_exception.InvalidBetException
          
    def placeBets(self, bet):
        """
        Player can call this method to place a bet on the Table.
        Multiple bets can be placed by calling multiple method multiple times. 
        """
        self.bets.append(bet)

