from . import craps_twobetplayer
from .martingale_betting import MartingaleBetting

class CrapsSevenCountPlayer(craps_twobetplayer.CrapsTwoBetPlayer):
    """
    Player that places 3 bets on the table.
    1. A Pass Line/Dont Pass Line bet when the point is off.
    2. A Pass Line Odds/Dont Pass Line odds bet when the point is on.
    3. A Number 7 proposition bet if the game lasts longer than 7 rounds.
    """

    def __init__(self, table, dice):
        self.dice = dice
        self.seven_strategy = MartingaleBetting(self.dice.all_outcomes.get('Number 7'))
        super().__init__(table, dice)
        self.throwCount = 0

    def placeBets(self, point):
        """
        places a bet if the player is ready to play another round and has enough in 
        its stake to place the bet.
        if its a come out roll, then places a line bet if not already present.
        if its a point roll, then places an odds bet.
        if the game lasts longer than 7 rounds, then places a number 7 proposition bet.

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
                self.throwCount = 0
            else:
                if 'Pass Line Odds' not in outcome_names \
                        and 'Dont Pass Line Odds' not in outcome_names:
                    self.oddsBet()
                elif self.throwCount >= 7 and 'Number 7' not in outcome_names:
                    self.table.placeBet(
                        self.seven_strategy.createBet(self)
                    )
                self.throwCount += 1
    
    def win(self, bet):
        """
        matches the winning parameter outcome with the seven strategy outcome and calls the 
        win method of the seven strategy.
        leaves the line and odds bet resolutions and stake adjustment to ancestors.

        :param bet: (Bet) 
        """
        if bet.outcome == self.seven_strategy.outcome:
            self.seven_strategy.win()
        super().win(bet)

    def lose(self, bet):
        """
        matches the losing parameter outcome with the  outcome and calls the 
        loss method of the seven strategy.
        leaves the line and odds bet resolutions and stake adjustment to ancestors.

        :param bet: (Bet)
        """
        if bet.outcome == self.seven_strategy.outcome:
            self.seven_strategy.lose()
        super().lose(bet)
