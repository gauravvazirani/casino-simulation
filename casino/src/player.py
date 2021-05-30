from abc import abstractmethod,ABCMeta

class Player(metaclass=ABCMeta):
    """
    An abstract class defining the behavior of a player playing a game of casino.
    """

    def __init__(self, stake, event_factory):
        self.stake = stake

    @staticmethod
    @abstractmethod
    def playing():
        """
        Returns True if player is still active
        """

    @staticmethod
    @abstractmethod
    def placeBets():
        """
        place a bet on outcome 'Black' on the table
        update the stake based on bet amount

        :param table: (Table)
        :param wheel: (Wheel)
        """

    def win(self, bet):
        """
        update stake with the winning amount
        update bet_amount to initlal value
        reduce rounds left to 1 less than that of current value 

        :param bet: (Bet)
        """
        self.stake += bet.winAmount()

    def lose(self):
        """
        update bet_amount to 2 times the current value 
        reduce rounds left to 1 less than that of current value 

        :param bet: (Bet)
        """
        pass
    
    @staticmethod
    @abstractmethod
    def setStake():
        """
        Set stake value before simulation of a session of game play
        """

    @staticmethod
    @abstractmethod
    def setRounds():
        """
        Set rounds_to_go value before simulation of a session of game play
        """
    
