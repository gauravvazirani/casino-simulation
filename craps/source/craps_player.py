import outcome 
import player
import bet

class CrapsPlayer(player.IPlayer):

    def __init__(self, table):
        self.table = table
        self.stake = 10000 
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

    def placeBets(self):
        pass

    def win(self, bet):
        self.stake += bet.winAmount()

    def lose(self, bet):
        pass

    def winners(self):
        pass
    
