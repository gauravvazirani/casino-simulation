import bet
import player

class RoulettePlayer(player.Player):

    def __init__(self, table, wheel):
        super().__init__(stake=1000)
        self.table = table
        self.wheel = wheel
        #self.stake = 100 * initial_bet_amount 
        self.rounds_to_go = 250
    
    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if self.rounds_to_go > 0 and self.stake >= self.table.minimum \
              else False

    def placeBets(self):
        black = self.wheel.all_outcomes.get('Black')
        self.table.placeBet(bet.Bet(10 ,black))
        self.stake -= self.bet_amount
    