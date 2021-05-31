from . import bet 

# class PlayerStateFactory():
    
#     def __init__(self, player, outcome):
#         self.values = {
#             'nowins': PlayerNoWins(player, outcome),
#             'onewin': PlayerOneWin(player, outcome),
#             'twowins': PlayerTwoWins(player, outcome),
#             'threewins': PlayerThreeWins(player, outcome)
#         }

#     def get(self, name):
#         return self.values.get(name)


class Player1326State():
    """
    A base class implementing the common features of a set of states used in 
    1-3-2-6 betting strategy.    
    """

    def __init__(self, player, bet_multiple, outcome, next_state_win):
        self.player = player 
        self.bet_multiple = bet_multiple
        self.outcome = outcome
        self.next_state_win = next_state_win

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
        return self.next_state_win

    def nextLost(self):
        """
        :return: (state) resets the current state of the player to no wins.
        """
        return PlayerNoWins(self.player, self.outcome)

class PlayerNoWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 1, outcome, PlayerOneWin(self.player, self.outcome))

class PlayerOneWin(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 3, outcome, PlayerTwoWins(self.player, self.outcome))

class PlayerTwoWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 2, outcome, PlayerThreeWins(self.player, self.outcome))

class PlayerThreeWins(Player1326State):
    def __init__(self, player, outcome):
        super().__init__(player, 6, outcome, PlayerNoWins(self.player, self.outcome))
