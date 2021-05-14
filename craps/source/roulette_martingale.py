import roulette_player
import bet

class RouletteMartingale(roulette_player.RoulettePlayer):

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.initial_bet_amount = 10
        self.rounds_to_go = 250
        self.loss_count = 0
              
    def placeBets(self):
        bet_multiple = 2**self.loss_count
        bet_amount = self.initial_bet_amount * bet_multiple
        black = self.wheel.all_outcomes.get('Black')
        self.table.placeBet(bet.Bet(bet_amount ,black))
        self.stake -= self.bet_amount
    
    def win(self, bet):
        super().win(bet)
        self.loss_count = 0 

    def lose(self):
        self.loss_count += 1
