from . import table
from . import bin_builder
from . import game
from . import seven_reds
from . import simulator

if __name__ == '__main__':
    """
    Main file to control the casino application.
    
    """
    wheel = bin_builder.WheelDirector().construct()
    table = table.Table()
    game = game.Game(wheel, table)
    player = seven_reds.SevenReds(table, wheel, initial_bet_amount=10)
    sim = simulator.Simulator(game, player)
    sim.gather()
