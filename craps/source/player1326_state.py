import bet 

class Player1326State():

    def __init__(self, player):
        self.player = player 

    def currentBet(self):
        return NotImplemented

    def nextWon(self):
        return NotImplemented

    def nextLost(self):
        return Player1326NoWins(self.player)

class Player1326NoWins(Player1326State):
    def __init__(self, player):
        super().__init__(player)
        self.bet_multiple = 1

    def currentBet(self):
        return bet.Bet(self.bet_multiple*self.player.initial_bet_amount, self.player.outcome) 

    def nextWon(self):
        return Player1326OneWin(self.player)

class Player1326OneWin(Player1326State):
    def __init__(self, player):
        super().__init__(player)
        self.bet_multiple = 3

    def currentBet(self):
        return bet.Bet(self.bet_multiple*self.player.initial_bet_amount, self.player.outcome) 

    def nextWon(self):
        return Player1326TwoWins(self.player)

class Player1326TwoWins(Player1326State):
    def __init__(self, player):
        super().__init__(player)
        self.bet_multiple = 2

    def currentBet(self):
        return bet.Bet(self.bet_multiple*self.player.initial_bet_amount, self.player.outcome) 

    def nextWon(self):
        return Player1326ThreeWins(self.player)

class Player1326ThreeWins(Player1326State):
    def __init__(self, player):
        super().__init__(player)
        self.bet_multiple = 6

    def currentBet(self):
        return bet.Bet(self.bet_multiple*self.player.initial_bet_amount, self.player.outcome) 

    def nextWon(self):
        return Player1326NoWins(self.player)

