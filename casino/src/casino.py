from . import table
from . import simulator
from . import wheel
from . import roulette_random
from . import roulette_cancellation
from . import roulette_martingale
from . import roulette_seven_reds
from . import roulette1326
from . import roulette_fibonacci
from . import roulette_game
from . import craps_game 
from . import craps_onebetplayer
from . import craps_twobetplayer
from . import craps_sevencountplayer
from . import dice

class Casino():
    """
    Main file to control the casino application.
    """

    def __init__(self, game_type='roulette', player_type='random'):
            self.game_type = game_type
            self.player_type = player_type
            event_factory_map = {
                'craps' : dice.Dice,
                'roulette' : wheel.Wheel 
            }
            player_map = {
                'craps' : {
                    'onebet': craps_onebetplayer.OneBetPlayer,
                    'twobet': craps_twobetplayer.CrapsTwoBetPlayer,
                    'sevenbet': craps_sevencountplayer.CrapsSevenCountPlayer
                },
                'roulette' : {
                    'random': roulette_random.RouletteRandom,
                    'cancellation': roulette_cancellation.RouletteCancellation,
                    'martingale': roulette_martingale.RouletteMartingale,
                    'seven_reds': roulette_seven_reds.RouletteSevenReds,
                    '1326': roulette1326.Roulette1326,
                    'fibonacci': roulette_fibonacci.RouletteFibonacci
                }
            }
            game_map = {
                'roulette':roulette_game.RouletteGame,
                'craps': craps_game.CrapsGame
            }
            table_obj = table.Table(minimum=1, maximum=10000)
            event_factory = event_factory_map.get(self.game_type)()
            game = game_map[self.game_type](event_factory, table_obj)
            player = player_map[self.game_type][self.player_type](table_obj, event_factory)
            player.setStake(10000)
            player.setRounds(250)
            self.sessions = 50
            self.sim = simulator.Simulator(game, player)
 
    def play(self):  
        self.sim.gather(self.sessions)
        
    def save(self, fname):    
        self.sim.save(fname)
        