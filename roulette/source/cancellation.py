import player
import bet

class Cancellation(player.IPlayer):
    def __init__(self, wheel, table):
        self.wheel = wheel
        self.table = table
        self.stake = 1000
        self.sequence = self.resetSequence()
        self.outcome = self.wheel.all_outcomes.get('Black')
        if len(self.sequence)==1:
            self.bet_amount = self.sequence[0]
        elif len(self.sequence)>1:
            self.bet_amount = self.sequence[0] + self.sequence[-1] 

    def resetSequence(self):
        return [num for num in range(1,7)]

    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if self.rounds_to_go > 0 and self.sequence \
            and self.bet_amount <= self.stake \
              else False

    def placeBets(self):
        _bet = bet.Bet(amount=self.bet_amount, outcome=self.outcome)  
        self.table.placeBet(_bet)
        self.stake -= self.bet_amount
        
    def win(self, bet):
        self.stake += bet.winAmount()
        del self.sequence[0]
        if self.sequence:
            del self.sequence[-1]
        self.update_amount()

    def lose(self, bet):
        self.sequence.append(self.sequence[0]+self.sequence[-1])
        self.update_amount()

    def update_amount(self):
        if len(self.sequence)==1:
            self.bet_amount = self.sequence[0]
        elif len(self.sequence)>1:
            self.bet_amount = self.sequence[0] + self.sequence[-1] 

    def winners(self, winning_outcomes):
        pass
