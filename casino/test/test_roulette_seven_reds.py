import unittest
from src import roulette_seven_reds
from src import wheel
from src import table
from src import game
from unittest.mock import Mock, MagicMock

class TestSevenReds(unittest.TestCase):
    def setUp(self):
        self.wheel = wheel.Wheel()
        self.table = table.Table(minimum=1, maximum=1000)
        self.player = roulette_seven_reds.RouletteSevenReds(self.table, self.wheel)
        self.red = [self.wheel.all_outcomes['Red']]
        self.black = [self.wheel.all_outcomes['Black']]
        self.wheel.rng = Mock()
        self.wheel.rng.randint = Mock(return_value=1)
        self.game = game.Game(self.wheel, self.table)

    def test_winners(self):
        """
        Checks the updation of red_count variable is down correctly 
        for various sequences of reds and blacks.
        """
        self.player.winners(self.black)
        self.assertEqual(self.player.red_count, 7)
        for index in range(1,6):
            self.player.winners(self.red)
            self.assertEqual(self.player.red_count, 7-index)
        self.player.winners(self.black)
        self.assertEqual(self.player.red_count, 7)
        for index in range(1,10):
            self.player.winners(self.red)
        self.assertEqual(self.player.red_count, 0)
    
    def test_placeBets(self):
        """
        Assures that no bets have been placed until
        7 reds have been seen.
        """
        self.player.red_count=7
        self.player.placeBets()
        self.assertEqual(len(self.table.bets), 0)

        self.player.red_count=3
        self.player.placeBets()
        self.assertEqual(len(self.table.bets), 0)

        self.player.red_count=0
        self.player.placeBets()
        self.assertEqual(len(self.table.bets), 1)

    def test_martingale_system(self):
        """
        Assures that the martingale system is being followed along 
        with the seven reds logic.
        """
        self.assertEqual(self.player.loss_count, 0) 
        self.player.red_count=0
        self.game.cycle(self.player)
        self.assertEqual(self.player.loss_count, 1)

    def tearDown(self):
        self.wheel = None
        self.table = None
        self.player = None
        self.red = None 
        self.black = None

if __name__ == '__main__':
    unittest.main()
