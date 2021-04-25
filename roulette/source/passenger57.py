import bet
import player

class Passenger57(player.IPlayer):

    def __init__(self, stake, bet_amount, rounds_to_go):
        self.stake = stake
        self.amount = bet_amount
        self.rounds_to_go = rounds_to_go

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

    def lose(self, bet):
        self.rounds_to_go -= 1
