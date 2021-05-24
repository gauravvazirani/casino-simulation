from . import bet 

class Player1326State():

    def __init__(self, player, bet_multiple, outcome):
        self.player = player 
        self.bet_multiple = bet_multiple
        self.outcome = outcome

    def currentBet(self):
        return bet.Bet(self.bet_multiple*self.player.initial_bet_amount, 
            self.outcome) 

    def nextWon(self):
        return NotImplemented

    def nextLost(self):
        return PlayerNoWins(self.player, self.outcome)

class PlayerNoWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 1, outcome)

    def nextWon(self):
        return PlayerOneWin(self.player, self.outcome)

class PlayerOneWin(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 3, outcome)

    def nextWon(self):
        return PlayerTwoWins(self.player, self.outcome)

class PlayerTwoWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 2, outcome)

    def nextWon(self):
        return PlayerThreeWins(self.player, self.outcome)

class PlayerThreeWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 6, outcome)

    def nextWon(self):
        return PlayerNoWins(self.player, self.outcome)
