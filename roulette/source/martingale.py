import player
import bet

class Martingale(player.IPlayer):

    def __init__(self, stake, initial_bet_amount, rounds_to_go):
        self.stake = stake
        self.initial_bet_amount = initial_bet_amount
        self.amount = self.initial_bet_amount
        self.rounds_to_go = rounds_to_go
        self.loss_count = 0
        self.bet_multiple = 2 ** self.loss_count

    def playing(self):
        return True if self.rounds_to_go > 0 and self.amount <= self.stake \
              else False
              
    def placeBets(self, table, wheel):
        black = wheel.all_outcomes.get('Black')
        table.placeBet(bet.Bet(self.amount ,black))
        self.stake -= self.amount
    
    def win(self, bet):
        self.stake += bet.winAmount()
        self.rounds_to_go -= 1
        self.loss_count = 0 
        self.update_amount()

    def lose(self, bet):
        self.rounds_to_go -= 1
        self.loss_count += 1
        self.update_amount()

    def update_amount(self):
        self.bet_multiple = 2**self.loss_count
        self.amount = self.initial_bet_amount * self.bet_multiple
