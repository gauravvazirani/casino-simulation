import player
import bet
import player1326_state

class Player1326(player.IPlayer):

    def __init__(self, table, wheel, initial_bet_amount):
        self.table = table
        self.wheel = wheel
        self.initial_bet_amount = initial_bet_amount  
        self.stake = 100 * initial_bet_amount
        self.rounds_to_go = 250
        self.state = player1326_state.Player1326NoWins(self)
        self.outcome = self.wheel.all_outcomes.get('Black') 

    def setRounds(self, rounds_to_go):
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        self.stake = stake

    def playing(self):
        return True if self.rounds_to_go > 0 and self.state.bet_multiple * self.initial_bet_amount <= self.stake \
              else False
              
    def placeBets(self):
        bet = self.state.currentBet()
        self.table.placeBet(bet)
        self.stake -= bet.amount
    
    def win(self, bet):
        self.stake += bet.winAmount()
        self.state = self.state.nextWon()

    def lose(self, bet):
        self.state = self.state.nextLost()

    def winners(self, winning_outcomes):
        pass
