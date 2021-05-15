import craps_game
import roulette_game
import craps_player
import craps_martingale
import roulette_player
import table
import dice
import wheel

class CrapsSimulator():

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
