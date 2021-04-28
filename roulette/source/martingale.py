import player
import bet

class Martingale(player.IPlayer):

    def __init__(self, table, wheel, initial_bet_amount):
        self.table = table
        self.wheel = wheel
        self.initial_bet_amount = initial_bet_amount  
        self.bet_amount = initial_bet_amount
        self.stake = 100 * initial_bet_amount
        self.rounds_to_go = 250
        self.loss_count = 0
        self.bet_multiple = 2 ** self.loss_count

    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if self.rounds_to_go > 0 and self.bet_amount <= self.stake \
              else False
              
    def placeBets(self):
        black = self.wheel.all_outcomes.get('Black')
        self.table.placeBet(bet.Bet(self.bet_amount ,black))
        self.stake -= self.bet_amount
    
    def win(self, bet):
        self.stake += bet.winAmount()
        #self.rounds_to_go -= 1
        self.loss_count = 0 
        self.update_amount()

    def lose(self, bet):
        #self.rounds_to_go -= 1
        self.loss_count += 1
        self.update_amount()

    def update_amount(self):
        self.bet_multiple = 2**self.loss_count
        self.bet_amount = self.initial_bet_amount * self.bet_multiple

    def winners(self, winning_outcomes):
        pass
