from . import craps_game
from . import roulette_game
from . import craps_player
from . import craps_martingale
from . import roulette_player
from . import table
from . import dice
from . import wheel

class CrapsSimulator():
    """
    Class which simualtes Sessions of game play.
    It initialises the various components and stores the results after running
    a session of multiple cycles of play.
    """

    def __init__(self):
        # self.dice = dice.Dice()
        # self.table = table.Table(minimum=1, maximum=1000)
        # self.game = craps_game.CrapsGame(table=self.table, dice=self.dice)
        # self.table.setGame(self.game)
        # self.player = craps_player.CrapsPlayer(self.table)
        # self.player = craps_martingale.CrapsMartingale(self.table)

        self.wheel = wheel.Wheel()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game = roulette_game.RouletteGame(table=self.table, wheel=self.wheel)
        self.table.setGame(self.game)
        self.player = roulette_player.RoulettePlayer(self.table, self.wheel)

    def simulate(self):
        self.player.setRounds(3)
        self.game.cycle(player=self.player)

if __name__ == '__main__':
    simulator = CrapsSimulator()
    simulator.simulate()
