from . import player
from . import bet
from abc import abstractmethod

class CrapsSimplePlayer(player.Player):
    """
    Implementation of Player interface for the game of craps.
    """

    def __init__(self, table, line=None, odds=None):
        self.table = table
        super().__init__(stake=10000)
        self.rounds_to_go = 250
        self.bet_amount = 10
        self.line = line
        self.odds = odds

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

    def placeBets(self, point):
        """
        Player that places, 
        1. A Pass Line/Dont Pass Line bet when the point is off.
        2. A Pass Line Odds/Dont Pass Line odds bet when the point is on.
        """
        if self.rounds_to_go > 0 and self.bet_amount <= self.stake:
            outcome_names = [ _bet.outcome.name for _bet in self.table ]
            if point == 0:
                if 'Pass Line' not in outcome_names \
                    and 'Dont Pass Line' not in outcome_names:
                    pass_line_bet = bet.Bet(self.bet_amount , self.line)
                    self.table.placeBet(pass_line_bet)
                    self.stake -= pass_line_bet.price()
            else:
                if 'Pass Line Odds' not in outcome_names \
                    and 'Dont Pass Line Odds' not in outcome_names:
                    self.oddsBet()
        self.rounds_to_go -= 1

#    @abstractmethod
    def oddsBet(self):
        """
        override this method to configure odds bet strategy
        """ 
        pass_line_odds_bet = bet.Bet(self.bet_amount, self.odd, 
            player=self)
        self.table.placeBet(pass_line_odds_bet)
        self.stake -= pass_line_odds_bet.price()
