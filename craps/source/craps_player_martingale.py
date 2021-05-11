import craps_player
import bet
import outcome

class CrapsMartingale(craps_player.CrapsPlayer):

    def __init__(self, table):
        super().__init__(table)
        self.loss_count = 0
        self.bet_multiple = 1

    def placeBets(self, pointval):
        if self.rounds_to_go > 0:
            if pointval == 0:
                for _bet in self.table:
                    if _bet.outcome.name == 'Pass Line':
                        return 
                if self.stake >= self.bet_amount:        
                    pass_line_bet = bet.Bet(self.bet_amount ,outcome.Outcome('Pass Line', 1), player=self)
                    self.table.placeBet(pass_line_bet)
                    self.stake -= pass_line_bet.price()
            elif pointval > 0:
                for _bet in self.table:
                    if _bet.outcome.name == 'Pass Line Odds':
                        return
                current_amount = self.bet_multiple * self.bet_amount
                if current_amount <= self.stake:
                    pass_line_odds_bet = bet.Bet(current_amount ,outcome.Outcome('Pass Line Odds', 1), player=self)
                    self.table.placeBet(pass_line_odds_bet)
                    self.stake -= pass_line_odds_bet.price()

    def win(self, bet):
        super().win(bet)
        self.loss_count = 0

    def lose(self, bet):
        super().lose(bet)
        self.loss_count += 1
        self.bet_multiple *= 2
