import unittest
from unittest.mock import Mock, MagicMock
from src import table
from src import roulette_random
from src import roulette1326
from src import roulette_cancellation
from src import roulette_fibonacci
from src import simulator
from src import game
from src import bin_builder

class TestSimulator(unittest.TestCase):
    def setUp(self):
        self.table = table.Table(5,5000)
        self.wheel = bin_builder.WheelDirector().construct()
        self.wheel.rng = Mock()
        self.wheel.rng.randint = Mock(return_value=1)
        self.initial_bet_amount = 10
        # self.player = roulette_player_random.PlayerRandom(
        # self.player = roulette_passenger57.Passenger57(
        # self.player = roulette_player1326.Player1326(
        # self.player = roulette_cancellation.Cancellation(
        self.player = roulette_fibonacci.Fibonacci(
              table = self.table
             ,wheel = self.wheel
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
