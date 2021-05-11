import craps_player
import bet
import outcome

class CrapsPlayerPass(craps_player.CrapsPlayer):

    def placeBets(self, point):
        if self.rounds_to_go > 0 and self.bet_amount <= self.stake:
            if point == 0:
                for _bet in self.table:
                    if _bet.outcome.name == 'Pass Line':
                        return 
                pass_line_bet = bet.Bet(self.bet_amount ,outcome.Outcome('Pass Line', 1), player=self)
                self.table.placeBet(pass_line_bet)
                self.stake -= pass_line_bet.price()



