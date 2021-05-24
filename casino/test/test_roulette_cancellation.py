import wheel
from src import roulette_cancellation
from src import bet
from src import table
import unittest

class TestCancellation(unittest.TestCase):
    def setUp(self):
        self.wheel = wheel.Wheel()
        self.table = table.Table(minimum=10, maximum=1000)
        self.player = roulette_cancellation.RouletteCancellation(table=self.table, wheel=self.wheel)
        
    def test_placeBets(self):
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 1000)
        self.player.placeBets()
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.player.stake, 993)

    def test_win(self):
        self.assertEqual(len(self.player.sequence), 6)
        if len(self.player.sequence)==1:
            bet_amount = self.player.sequence[0]
        elif len(self.player.sequence)>1:
            bet_amount = self.player.sequence[0] + self.player.sequence[-1]
        self.player.win(bet.Bet(outcome=self.wheel.all_outcomes.get('Black'), amount=bet_amount))
        self.assertEqual(len(self.player.sequence), 4)
        self.assertEqual(len(self.player.sequence), 4)

    def test_lose(self):
        self.assertEqual(len(self.player.sequence), 6)
        self.player.lose()
        self.assertEqual(len(self.player.sequence), 7)
        self.assertEqual(self.player.sequence[-1], self.player.sequence[0]+self.player.sequence[-2])

    def tearDown(self):
        self.wheel = None
        self.table = None
        self.player = None         

if __name__ == '__main__':
    unittest.main()
