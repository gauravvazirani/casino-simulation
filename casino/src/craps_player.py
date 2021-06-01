from . import player
from . import bet
from abc import abstractmethod
from .config import PLAYER_STAKE, PLAYER_ROUNDS

class CrapsSimplePlayer(player.Player):
    """
    Implementation of Player interface for the game of craps.
    """

    def __init__(self, table, dice, line=None, odds=None):
        self.table = table
        super().__init__(dice)
        self.line = line
        self.odds = odds
        self.stake = PLAYER_STAKE
        self.rounds_to_go = PLAYER_ROUNDS

    def setRounds(self, rounds_to_go):
        """
        setter method for rounds_to_go

        :param rounds_to_go: (integer) number of rounds the player will play.
        """
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        """
        setter method for stake

        :param stake: (numeric) Net amount that player has in its wallet.
        """
        self.stake = stake

    def playing(self):
        """
        :return: (Boolean) whether or not player is ready to play the next round.
        """
        return True if (self.rounds_to_go > 0 and self.stake > 0) \
            or self.table.bets \
              else False

    @abstractmethod
    def placeBets(self, point, game):
        """
        override this method to configure line bet strategy
        """
        pass

    @abstractmethod
    def oddsBet(self):
        """
        override this method to configure odds bet strategy
        """ 
        pass
