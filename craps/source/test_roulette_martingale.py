import unittest
from unittest.mock import Mock, MagicMock
import game
import roulette_martingale
import table
import bin_builder

class TestGame(unittest.TestCase):
    """
    Class to test functionality of the Game class.
    In order to control outcome of the random number generator,
    mock object testing is used.
    """

    def setUp(self):
        _wheel = bin_builder.WheelDirector().construct()
        _wheel.rng = Mock()
        _wheel.rng.randint = Mock(return_value=1)
        _table = table.Table()
        self.game = game.Game(wheel=_wheel, table=_table)
        self.player = roulette_martingale.RouletteMartingale(wheel=_wheel, table=_table)

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
        self.game.cycle(self.player)
        self.assertEqual(self.player.stake, 2475)

    def tearDown(self):
        self.game = None
        self.player = None

if __name__ == '__main__':
    unittest.main()