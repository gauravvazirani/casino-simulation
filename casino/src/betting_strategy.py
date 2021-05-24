from abc import ABCMeta, abstractmethod

class BettingStrategy(metaclass=ABCMeta):

    def __init__(self, outcome, bet_amount):
        self.outcome = outcome
        self.bet_amount = bet_amount

    @staticmethod
    @abstractmethod
    def win(self):
        """
        """

    @staticmethod
    @abstractmethod
    def lose(self):
        """
        """

    @staticmethod
    @abstractmethod
    def createBet(self):
        """
        """

    def __str__(self):
        return f"{self.__class__.__name__}: outcome - {self.outcome}, amount - {self.bet_amount}"
