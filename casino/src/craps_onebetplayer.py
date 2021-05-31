from . import craps_player
from .nochange_betting import NoChangeBetting

class OneBetPlayer(craps_player.CrapsSimplePlayer):
    """
    Player that places a single bet on the table.
    A Pass Line/Dont Pass Line bet when the point is off.
    """

    def __init__(self, table, dice):
        self.table = table
        self.dice = dice
        self.line_strategy = NoChangeBetting(self.dice.all_outcomes.get('Pass Line'))
        super().__init__(table, dice)     

    def placeBets(self, point):
        """
        places a bet if the player is ready to play another round and has enough in 
        its stake to place the bet.
        if its a come out roll, then places a line bet if not already present.
        places no bet if the roll is a point roll.

        :param point: (integer) point on the board after the throw.
        """
        if self.rounds_to_go > 0 and self.bet_amount <= self.stake:
            outcome_names = [ _bet.outcome.name for _bet in self.table ]
            if point == 0:
                if 'Pass Line' not in outcome_names \
                    and 'Dont Pass Line' not in outcome_names:
                    pass_line_bet = self.line_strategy.createBet(self)
                    self.table.placeBet(pass_line_bet)
                    self.stake -= pass_line_bet.price()
            else:
                if 'Pass Line Odds' not in outcome_names \
                    and 'Dont Pass Line Odds' not in outcome_names:
                    self.oddsBet()

    def oddsBet(self):
        pass

    def win(self, bet):
        """
        matches the winning parameter outcome with the line outcome and calls the 
        win method of the line strategy.
        leaves the stake adjustment to ancestors.

        :param bet: (Bet) 
        """
        if bet.outcome == self.line_strategy.outcome:
            self.line_strategy.win()
        super().win(bet)

    def lose(self, bet):        
        """
        matches the losing parameter outcome with the line outcome and calls the 
        loss method of the line strategy.
        leaves the stake adjustment to ancestors.
        
        :param bet: (Bet) 
        """
        if bet.outcome == self.line_strategy.outcome:
            self.line_strategy.lose()
        super().lose()
        