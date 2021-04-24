import passenger57
import table
import bin_builder

class Game():
    """
    Class to perform simulation of a game of roulette
    """

    def __init__(self):
        self.wheel = bin_builder.WheelDirector().construct()
        self.table = table.Table()

    def cycle(self, player):
        """
        simulates a single round of single player roulette
        1 player places its bets
        2 game fetches the winning outcomes from a single
            spin of the wheel
        3 game updates player balances based on the 
            outcome being a winning or losing outcome.

        :param player: (Passenger57)
        """

        player.placeBets(self.table, self.wheel)
        winning_outcomes = self.wheel.next() 
        for bet in self.table:
            if bet.outcome in winning_outcomes:
                player.win(bet)
            else:
                player.lose(bet)
