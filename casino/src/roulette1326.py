from . import bet
from . import roulette_player
from . import player1326_state

class Roulette1326(roulette_player.RoulettePlayer):

    def __init__(self, table, wheel):
        super().__init__(table, wheel)
        self.initial_bet_amount = 10
        self.rounds_to_go = 250
        self.state = player1326_state.PlayerNoWins(
            self, 
            self.wheel.all_outcomes.get('Black')
            )

    def placeBets(self):
        bet = self.state.currentBet()
        self.table.placeBet(bet)
        self.stake -= bet.amount
    
    def win(self, bet):
        super().win(bet)
        self.state = self.state.nextWon()

    def lose(self):
        self.state = self.state.nextLost()
