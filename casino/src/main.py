# from . import table
# from . import game
# #from . import seven_reds
# from . import simulator
# from . import wheel
# from . import roulette_player

import table
import game
#  . import seven_reds
import simulator
import wheel
import roulette_player

if __name__ == '__main__':
    """
    Main file to control the casino application.
    """

    wheel = wheel.Wheel()
    table = table.Table(minimum=1, maximum=10000)
    game = game.Game(wheel, table)
    table.setGame(game)
    player = roulette_player.RoulettePlayer(table, wheel)
    sim = simulator.Simulator(game, player)
    player.setStake(10000)
    player.setRounds(250)
    sessions = 50
    sim.gather(sessions)
    sim.save('temp.csv')

    # self.dice = dice.Dice()
    # self.table = table.Table(minimum=1, maximum=10000)
    # self.game = craps_game.CrapsGame(table=self.table, dice=self.dice)
    # self.table.setGame(self.game)
    # self.player = craps_player.CrapsPlayer(self.table)
    # self.player = craps_martingale.CrapsMartingale(self.table)

    # self.wheel = wheel.Wheel()
    # self.table = table.Table(minimum=1, maximum=10000)
    # self.game = roulette_game.RouletteGame(table=self.table, wheel=self.wheel)
    # self.table.setGame(self.game)
    # self.player = roulette_player.RoulettePlayer(self.table, self.wheel)
