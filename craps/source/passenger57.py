import bet
import player

class Passenger57(player.IPlayer):

    def __init__(self, table, wheel, initial_bet_amount):
        self.table = table
        self.wheel = wheel
        self.stake = 100 * initial_bet_amount 
        self.rounds_to_go = 250
        self.bet_amount = initial_bet_amount
    
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

    def lose(self, bet):
        pass

    def winners(self, winning_outcomes):
        pass
