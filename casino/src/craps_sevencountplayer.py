from . import craps_twobetplayer

class CrapsSevenCountPlayer(craps_twobetplayer.CrapsTwoBetPlayer):
    """
    """

    def __init__(self, table, line_strategy, odds_strategy, seven_strategy):
        self.seven_strategy = seven_strategy
        super().__init__(table, line_strategy, odds_strategy)
        self.throwCount = 0

    def placeBets(self, point):
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
        if bet.outcome == self.seven_strategy.outcome:
            self.seven_strategy.win()
        super().win(bet)

    def lose(self, bet):
        if bet.outcome == self.seven_strategy.outcome:
            self.seven_strategy.lose()
        super().lose(bet)
