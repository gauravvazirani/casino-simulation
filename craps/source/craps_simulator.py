import craps_game
import craps_game_state
import craps_player_pass
import craps_player_martingale
import table
import throw_builder

class CrapsSimulator():

    def __init__(self):
        self.dice = throw_builder.DiceDirector().construct()
        self.table = table.CrapsTable()
        self.game = craps_game.CrapsGame(table=self.table, dice=self.dice)
        self.player = craps_player_martingale.CrapsMartingale(self.table)
    
    def simulate(self):
        self.player.setRounds(1)
        self.game.cycle(player=self.player)

if __name__ == '__main__':
    simulator = CrapsSimulator()
    simulator.simulate()