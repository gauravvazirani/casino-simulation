import bet 

class Roulette1326State():

    def __init__(self, player, bet_multiple):
        self.player = player 
        self.bet_multiple = bet_multiple

    def currentBet(self):
        return bet.Bet(self.bet_multiple*self.player.initial_bet_amount, self.player.outcome) 

    def nextWon(self):
        return NotImplemented

    def nextLost(self):
        return RouletteNoWins(self.player)

class RouletteNoWins(Roulette1326State):
    def __init__(self, player):
        super().__init__(player, 1)

    def nextWon(self):
        return RouletteOneWin(self.player)

class RouletteOneWin(Roulette1326State):
    def __init__(self, player):
        super().__init__(player, 3)

    def nextWon(self):
        return RouletteTwoWins(self.player)

class RouletteTwoWins(Roulette1326State):
    def __init__(self, player):
        super().__init__(player, 2)

    def nextWon(self):
        return RouletteThreeWins(self.player)

class RouletteThreeWins(Roulette1326State):
    def __init__(self, player):
        super().__init__(player, 6)

    def nextWon(self):
        return RouletteNoWins(self.player)
