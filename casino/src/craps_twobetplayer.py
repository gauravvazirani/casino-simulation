from . import craps_onebetplayer
from .bet1326_betting import Bet1326Betting

class CrapsTwoBetPlayer(craps_onebetplayer.OneBetPlayer):
    """
    Player that places 2 bets on the table.
    1. A Pass Line/Dont Pass Line bet when the point is off.
    2. A Pass Line Odds/Dont Pass Line odds bet when the point is on.
    """

    def __init__(self, table, dice, line_strategy):
        super().__init__(table, dice, line_strategy)
        self.dice = dice
        self.odds_strategy = Bet1326Betting(self.dice.all_outcomes.get('Pass Line Odds'))

    def oddsBet(self):
        """
        overrides the simple craps player odds method to 
        implement logic for placing the odds bet.
        """ 
        pass_line_odds_bet = self.odds_strategy.createBet(self) 
        self.table.placeBet(pass_line_odds_bet)
        self.stake -= pass_line_odds_bet.price()

    def win(self, bet):
        """
        matches the winning parameter outcome with the odds outcome and calls the 
        win method of the odds strategy.
        leaves the line bet resolution and stake adjustment to ancestors.

        :param bet: (Bet) 
        """
        if bet.outcome == self.odds_strategy.outcome:
            self.odds_strategy.win()
        super().win(bet)

    def lose(self, bet):
        """
        matches the losing parameter outcome with the odds outcome and calls the 
        loss method of the odds strategy.
        leaves the line bet resolution and stake adjustment to ancestors.
        """
        if bet.outcome == self.odds_strategy.outcome:
            self.odds_strategy.lose()
        super().lose(bet)
