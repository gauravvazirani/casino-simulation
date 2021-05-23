import craps_onebetplayer

class CrapsTwoBetPlayer(craps_onebetplayer.OneBetPlayer):

    def __init__(self, table, line_strategy, odds_strategy):
        self.table = table
        super().__init__(table, line_strategy)
        self.odds_strategy = odds_strategy     

    def oddsBet(self):
        """
        overwrite this method to configure odds bet strategy
        """ 
        pass_line_odds_bet = self.odds_strategy.createBet(self) 
        self.table.placeBet(pass_line_odds_bet)
        self.stake -= pass_line_odds_bet.price()

    def win(self, bet):
        if bet.outcome == self.odds_strategy.outcome:
            self.odds_strategy.win()
        super().win(bet)

    def lose(self, bet):
        if bet.outcome == self.odds_strategy.outcome:
            self.odds_strategy.lose()
        super().lose(bet)
