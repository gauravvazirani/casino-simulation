import bet
import roulette_player
import roulette1326_state

class Roulette1326(roulette_player.RoulettePlayer):

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.initial_bet_amount = 10
        self.rounds_to_go = 250
        self.state = roulette1326_state.Roulette1326NoWins(self)
        self.outcome = self.wheel.all_outcomes.get('Black') 

    def placeBets(self):
        bet = self.state.currentBet()
        self.table.placeBet(bet)
        self.stake -= bet.amount
    
    def win(self, bet):
        super().win(bet)
        self.state = self.state.nextWon()

    def lose(self, bet):
        self.state = self.state.nextLost()
