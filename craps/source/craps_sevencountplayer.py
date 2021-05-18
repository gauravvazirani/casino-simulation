import craps_twobetplayer
import bet
import outcome
import nochange_betting

class CrapsSevenCountPlayer(craps_twobetplayer.CrapsTwoBetPlayer):

    def __init__(self, table):
        self.table = table
        self.line_strategy = nochange_betting.NochangeBetting(
            outcome.Outcome('Pass Line', 1)
            )
        self.odds_strategy = nochange_betting.NochangeBetting(
            outcome.Outcome('Pass Line Odds', 1)
            )
        self.seven_strategy = nochange_betting.NochangeBetting(
            outcome.Outcome('Number 7', 4)
            )
        super().__init__(table, self.line_strategy, self.odds_strategy)
        self.throwCount = 0

    def placeBets(self, point):
        if self.rounds_to_go > 0 and self.bet_amount <= self.stake:
            outcome_names = [ _bet.outcome.name for _bet in self.table ]
            if point == 0:
                if 'Pass Line' not in outcome_names \
                    and 'Dont Pass Line' not in outcome_names:
                    pass_line_bet = self.strategy.createBet(self)
                    self.table.placeBet(pass_line_bet)
                    self.stake -= pass_line_bet.price()
                    self.throwCount = 0
            elif 'Pass Line Odds' not in outcome_names \
                and 'Dont Pass Line Odds' not in outcome_names:
                self.oddsBet()
            elif self.throwCount > 7:
                self.table.placeBet(
                    self.seven_strategy.createBet(self)
                )
                self.throwCount += 1
                
