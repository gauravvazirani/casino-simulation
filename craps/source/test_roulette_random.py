import unittest
import roulette_random
import table
import bin_builder
from unittest.mock import Mock, MagicMock

class Test(unittest.TestCase):
    """
    Class to test functionality of random player strategy
    using mock object testing to test bet placement   
    """
    def setUp(self):
        self.wheel = bin_builder.WheelDirector().construct()
        self.table = table.Table()
        self.player = roulette_random.RouletteRandom(table=self.table, wheel=self.wheel)
        self.player.rng = Mock()
        self.player.rng.randint = Mock(side_effect=range(len(self.player.outcomes)))

    def test_placeBets(self):
        """
        random player random number generator should place bets without any errors
        for all outcomes
        """
        for i in range(len(self.player.outcomes)):
            self.player.placeBets()
        self.assertEqual(len(self.table.bets), len(self.player.outcomes)) 

    def tearDown(self):
        self.wheel = None
        self.table = None
        self.player = None

if __name__ == '__main__':
    unittest.main()