from . import table
from . import simulator
from . import wheel
from . import roulette_random
from . import roulette_cancellation
from . import roulette_martingale
from . import roulette_seven_reds
from . import roulette1326
from . import roulette_game
from . import craps_game 
from . import craps_onebetplayer
from . import dice

class Casino():
    """
    Main file to control the casino application.
    """

    def __init__(self, game_type='roulette', player_type='random'):
            self.game_type = game_type
            self.player_type = player_type
            _table = table.Table(minimum=1, maximum=10000)
            self.event_factory_map = {
                'craps' : dice.Dice(),
                'roulette' : wheel.Wheel() 
            }
            self.event_factory = self.event_factory_map[self.game_type]
            self.player_map = {
                'craps' : {
                    'onebet': craps_onebetplayer.OneBetPlayer(_table)
                }
                ,
                'roulette' : {
                    'random': roulette_random.RouletteRandom(_table, self.event_factory_map['roulette']),
                    'cancellation': roulette_cancellation.RouletteCancellation(_table, self.event_factory_map['roulette']),
                    'martingale': roulette_martingale.RouletteMartingale(_table, self.event_factory_map['roulette']),
                    'seven_reds': roulette_seven_reds.RouletteSevenReds(_table, self.event_factory_map['roulette']),
                    '1326': roulette1326.Roulette1326(_table, self.event_factory_map['roulette'])
                }
            }
            self.game_map = {
                'roulette':roulette_game.RouletteGame(self.event_factory_map['roulette'], _table),
                'craps': craps_game.CrapsGame(self.event_factory_map['craps'], _table)
            }
            game = self.game_map[self.game_type]
            _table.setGame(game)
            player = self.player_map[self.game_type][self.player_type]
            self.sim = simulator.Simulator(game, player)
            player.setStake(10000)
            player.setRounds(250)
            self.sessions = 50
 
    def play(self):  
        self.sim.gather(self.sessions, self.event_factory)
        
    def save(self, fname):    
        self.sim.save(fname)
        