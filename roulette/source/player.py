from abc import abstractmethod,ABCMeta

class IPlayer(metaclass=ABCMeta):

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

    @staticmethod
    @abstractmethod
    def win():
        """
        update stake with the winning amount
        update bet_amount to initlal value
        reduce rounds left to 1 less than that of current value 

        :param bet: (Bet)
        """

    @staticmethod
    @abstractmethod
    def lose():
        """
        update bet_amount to 2 times the current value 
        reduce rounds left to 1 less than that of current value 

        :param bet: (Bet)
        """

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

