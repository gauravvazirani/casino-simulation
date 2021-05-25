import unittest
from unittest.mock import Mock, MagicMock
from src import roulette_game
from src import roulette_player
from src import table
from src import wheel

class TestGame(unittest.TestCase):
    """
    Class to test functionality of the Game class.
    In order to control outcome of the random number generator,
    mock object testing is used.
    """

    def setUp(self):
        _wheel = wheel.Wheel()
        _wheel.rng = Mock()
        _wheel.rng.randint = Mock(return_value=1)
        self.table = table.Table(minimum=1, maximum=1000)
        self.game = roulette_game.RouletteGame(wheel=_wheel, table=self.table)
        self.table.setGame(self.game)
        self.player = roulette_player.RoulettePlayer(wheel=_wheel, table=self.table)

    def test_setStake(self):
        self.player.setStake(1000)
        self.assertEqual(self.player.stake,1000)

    def test_setRounds(self):
        self.player.setRounds(6)
        self.assertEqual(self.player.rounds_to_go,6)

    def test_cycle(self):
        """
        Run a test simulation of the game by calling the cycle method.  
        If the simulation works correctly the player should win\lose the 
        bet and player balance should be updated to balance +\- bet_amount. 
        """
        self.player.setStake(2500)
        self.game.cycle(self.player)
        self.assertEqual(self.player.stake, 2490)

    def tearDown(self):
        self.game = None
        self.player = None

if __name__ == '__main__':
    unittest.main()
    