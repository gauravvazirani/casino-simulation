from abc import ABCMeta, abstractmethod

class BettingStrategy(metaclass=ABCMeta):
    """
    Abstract class that defines behavior of a betting strategy.
    """

    def __init__(self, outcome, bet_amount):
        self.outcome = outcome
        self.bet_amount = bet_amount

    @staticmethod
    @abstractmethod
    def win(self):
        """
        Each strategy must override this method to implement 
        its own logic after a win.
        """

    @staticmethod
    @abstractmethod
    def lose(self):
        """
        Each strategy must override this method to implement 
        its own logic after a loss.
        """

    @staticmethod
    @abstractmethod
    def createBet(self):
        """
        Each strategy must override this method to implement 
        its own logic to create a bet.
        """

    def __str__(self):
        """
        :return: (string) of the form <Strategy name> : outcome - <outcome object>, amount - <bet amount> 
        """
        return f"{self.__class__.__name__}: outcome - {self.outcome}, amount - {self.bet_amount}"
