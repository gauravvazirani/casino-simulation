from . import game

class RouletteGame(game.Game):

    def __init__(self, wheel, table):
        super().__init__(wheel, table)

    def cycle(self, player):
        """
        simulates a single round of single player roulette
        1 player places its bets
        2 game fetches the winning outcomes from a 
        single spin of the wheel
        3 game updates player balances based on the outcome being a 
        winning or losing outcome.

        :param player: (Passenger57)
        """    
        player.placeBets()
        self.table.allValid()
        winning_outcomes = self.eventFactory.next()
        for bet in list(self.table):
            if bet.outcome in winning_outcomes:
                player.win(bet)
            else:
                player.lose()
            self.table.bets.remove(bet)

    def isValid(self, outcome):
        return True
