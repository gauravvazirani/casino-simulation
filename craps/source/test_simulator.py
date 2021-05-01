import unittest
from unittest.mock import Mock, MagicMock
import table
import passenger57
import simulator
import game
import bin_builder
import player_random
import player1326
import cancellation
import fibonacci

class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.table = table.Table()
        self.wheel = bin_builder.WheelDirector().construct()
        self.wheel.rng = Mock()
        self.wheel.rng.randint = Mock(return_value=1)
        self.initial_bet_amount = 10
        # self.player = player_random.PlayerRandom(
        # self.player = passenger57.Passenger57(
        # self.player = player1326.Player1326(
        # self.player = cancellation.Cancellation(
        self.player = fibonacci.Fibonacci(
              table = self.table
             ,wheel = self.wheel
#             ,self.initial_bet_amount
             )
        self.game = game.Game(self.wheel, self.table)

    def test_session(self):
        print("Simulating a Single Session of 5 cycles")
        self.simulator = simulator.Simulator(self.game, self.player, init_duration=5, stake=300)
        duration, max_stake = self.simulator.session(debug=True)
        print(f"Session Duration: {duration},Max Stake: {max_stake}")

    def test_gather(self):
        print("Simulation 50 Sessions of 250 cycles each")
        self.simulator = simulator.Simulator(self.game, self.player, stake=10000, init_duration=10)
        self.simulator.gather()
    
    def tearDown(self):
        self.table = None
        self.wheel = None
        self.initial_bet_amount = None
        self.player = None
        self.game = None

if __name__ == "__main__":
    unittest.main()
