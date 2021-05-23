import craps_player

class OneBetPlayer(craps_player.CrapsSimplePlayer):

    def __init__(self, table, strategy):
        self.table = table
        self.line_strategy = strategy
        super().__init__(table)     

    def placeBets(self, point):
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
        if bet.outcome == self.line_strategy.outcome:
            self.line_strategy.win()
        super().win(bet)

    def lose(self, bet):
        if bet.outcome == self.line_strategy.outcome:
            self.line_strategy.lose()
        super().lose()
        return