import outcome 
import player
import bet

class CrapsPlayer(player.Player):

    def __init__(self, table):
        self.table = table
        super().__init__(stake=10000)
        self.rounds_to_go = 250
        self.bet_amount = 10

    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if (self.rounds_to_go > 0 and self.stake > 0) \
            or self.table.bets \
              else False

    def placeBets(self, point):
        if self.rounds_to_go > 0 and self.bet_amount <= self.stake:
            if point == 0:
                for _bet in self.table:
                    if _bet.outcome.name == 'Pass Line':
                        return 
                pass_line_bet = bet.Bet(self.bet_amount ,outcome.Outcome('Pass Line', 1), player=self)
                self.table.placeBet(pass_line_bet)
                self.stake -= pass_line_bet.price()
