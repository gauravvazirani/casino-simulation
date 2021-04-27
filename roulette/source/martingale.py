import player
import bet

class Martingale(player.IPlayer):

    def __init__(self, table, wheel, initial_bet_amount):
        self.table = table
        self.wheel = wheel
        self.initial_bet_amount = initial_bet_amount  
        self.amount = initial_bet_amount
        self.stake = 100 * table.minimum
        self.rounds_to_go = 250
        self.loss_count = 0
        self.bet_multiple = 2 ** self.loss_count

    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if self.rounds_to_go > 0 and self.amount <= self.stake \
              else False
              
    def placeBets(self):
        black = self.wheel.all_outcomes.get('Black')
        self.table.placeBet(bet.Bet(self.amount ,black))
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
