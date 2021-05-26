from . import bet 

class Player1326State():
    """
    A base class implementing the common features of a set of states used in 
    1-3-2-6 betting strategy.    
    """

    def __init__(self, player, bet_multiple, outcome):
        self.player = player 
        self.bet_multiple = bet_multiple
        self.outcome = outcome

    def currentBet(self):
        """
        :return: (Bet) bet based on the current value of the multiplier.
        """
        return bet.Bet(self.bet_multiple*self.player.initial_bet_amount, 
            self.outcome) 

    def nextWon(self):
        """
        leaves implementation to the specific state classes. 
        """
        return NotImplemented

    def nextLost(self):
        """
        :return: (state) resets the current state of the player to no wins.
        """
        return PlayerNoWins(self.player, self.outcome)

class PlayerNoWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 1, outcome)

    def nextWon(self):
        """
        :return: (state) resets the current state of the player to one win.
        """
        return PlayerOneWin(self.player, self.outcome)

class PlayerOneWin(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 3, outcome)

    def nextWon(self):
        """
        :return: (state) resets the current state of the player to two wins.
        """        
        return PlayerTwoWins(self.player, self.outcome)

class PlayerTwoWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 2, outcome)

    def nextWon(self):
        """
        :return: (state) resets the current state of the player to three wins.
        """
        return PlayerThreeWins(self.player, self.outcome)

class PlayerThreeWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 6, outcome)

    def nextWon(self):
        """
        :return: (state) resets the current state of the player to no wins.
        """
        return PlayerNoWins(self.player, self.outcome)
