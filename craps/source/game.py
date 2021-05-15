from abc import abstractmethod,ABCMeta

class Game(metaclass=ABCMeta):
    """
    Class to perform simulation of a game of roulette
    """

    def __init__(self, eventFactory, table):
        self.eventFactory = eventFactory
        self.table = table
    
    @staticmethod
    @abstractmethod
    def cycle(self, player):
        """
        simulates a single round of single player roulette
        1 player places its bets
        2 game fetches the winning outcomes from a 
        single spin of the wheel
        3 game updates player balances based on the outcome being a 
        winning or losing outcome.

        :param player: (Passenger57)
        """    
                
    def reset(self):
        self.table.clear()
