import craps_player
import bet
import outcome

class CrapsMartingale(craps_player.CrapsSimplePlayer):

    def __init__(self, table):
        super().__init__(table)
        self.loss_count = 0
        self.bet_multiple = 1

    def oddsBet(self):
        current_amount = self.bet_multiple * self.bet_amount
        if current_amount <= self.stake:
            pass_line_odds_bet = bet.Bet(current_amount, self.odd, 
                player=self)
            self.table.placeBet(pass_line_odds_bet)
            self.stake -= pass_line_odds_bet.price()

    def win(self, bet):
        super().win(bet)
        self.loss_count = 0

    def lose(self):
        self.loss_count += 1
        self.bet_multiple *= 2
