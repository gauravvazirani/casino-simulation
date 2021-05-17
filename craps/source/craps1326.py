import bet
import craps_player
import player1326_state

class Craps1326(craps_player.CrapsSimplePlayer):

    def __init__(self, table, line, odds):
        super().__init__(table, line, odds)
        self.initial_bet_amount = 10
        self.rounds_to_go = 250
        self.state = player1326_state.PlayerNoWins(
            self, 
            self.odds
            )

    def oddsBet(self):
        bet = self.state.currentBet()
        self.table.placeBet(bet)
        self.stake -= bet.price()
    
    def win(self, bet):
        super().win(bet)
        self.state = self.state.nextWon()

    def lose(self):
        self.state = self.state.nextLost()
