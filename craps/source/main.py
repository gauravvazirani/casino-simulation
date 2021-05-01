import table
import bin_builder
import game
import seven_reds
import simulator

if __name__ == '__main__':
    wheel = bin_builder.WheelDirector().construct()
    table = table.Table()
    game = game.Game(wheel, table)
    player = seven_reds.SevenReds(table, wheel, initial_bet_amount=10)
    sim = simulator.Simulator(game, player)
    sim.gather()
