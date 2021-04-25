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
        round_no = 1
        while player.playing():
            print(f"Starting Round {round_no}")
            print(f"Player Balance : {player.stake} points")
            print(f"Bet Amount: {player.amount} points")
            self.table.bets=[]
            player.placeBets(self.table, self.wheel)
            self.table.isValid()
            winning_outcomes = self.wheel.next() 
            for bet in self.table:
                if bet.outcome in winning_outcomes:
                    print("Congratulations! Player Wins")
                    player.win(bet)
                else:
                    print("Player Lost...")
                    player.lose(bet)
            round_no += 1
            print(f"Updated player Balance: {player.stake} points\n")
