import unittest
from unittest.mock import Mock, MagicMock
import game
import passenger57

class TestGame(unittest.TestCase):
    """
    Class to test functionality of the Game class.
    In order to control outcome of the random number generator,
    mock object testing is used.
    """

    def setUp(self):
        self.game = game.Game()
        self.game.wheel.rng = Mock()
        self.game.wheel.rng.randint = Mock(return_value=1)
        self.player = passenger57.Passenger57()

    def test_cycle(self):
        """
        Run a test simulation of the game by calling the cycle method.  
        If the simulation works correctly the player should lose the 
        bet and player balance should be updated to balance - bet_amount. 
        """
        self.game.cycle(self.player)
        self.assertEqual(self.player.balance,990)

    def tearDown(self):
        self.game = None
        self.player = None


if __name__ == '__main__':
    unittest.main()