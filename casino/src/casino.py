from . import table
from . import simulator
from . import wheel
from . import roulette_random
from . import roulette_game
from . import craps_game 
from . import craps_onebetplayer
from . import dice

class Casino():
    """
    Main file to control the casino application.
    """

    # player_factory = {
    #     'craps' : {
    #         'onebet': craps_onebetplayer.OneBetPlayer(table)
    #     },
    #     'roulette' : {
    #         'random': roulette_random.RouletteRandom(table, wheel)
    #     }
    # }
    # game_factory = {
    #     'roulette':roulette_game.RouletteGame(wheel, table),
    #     'craps': craps_game.CrapsGame(dice, table)
    # }

    def __init__(self, game_type=None, player_type=None):
            self.game_type = game_type
            self.player_type = player_type
            _wheel = wheel.Wheel()
            _dice = dice.Dice()
            _table = table.Table(minimum=1, maximum=10000)
            # game = game_factory[self.game_type][self.player_type]
            game = roulette_game.RouletteGame(_wheel, _table)
            _table.setGame(game)
            # player = player_factory[self.player_type]
            player = roulette_random.RouletteRandom(_table, _wheel)
            self.sim = simulator.Simulator(game, player)
            player.setStake(10000)
            player.setRounds(250)
            self.sessions = 50
 
    def play(self):  
        self.sim.gather(self.sessions)
        
    def save(self, fname):    
        self.sim.save(fname)
        