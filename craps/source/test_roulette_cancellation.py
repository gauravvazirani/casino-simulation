import bin_builder
import roulette_cancellation
import bet
import table
import unittest

class TestCancellation(unittest.TestCase):
    def setUp(self):
        self.wheel = bin_builder.WheelDirector().construct()
        self.table = table.Table()
        self.player = roulette_cancellation.RouletteCancellation(table=self.table, wheel=self.wheel)
        
    def test_placeBets(self):
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 1000)
        self.player.placeBets()
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.player.stake, 993)

    def test_win(self):
        self.assertEqual(len(self.player.sequence), 6)
        self.player.win(bet.Bet(outcome=self.player.outcome, amount=self.player.bet_amount))
        self.assertEqual(len(self.player.sequence), 4)
        self.assertEqual(len(self.player.sequence), 4)
        self.assertEqual(self.player.bet_amount, self.player.sequence[0]+self.player.sequence[-1])

    def test_lose(self):
        self.assertEqual(len(self.player.sequence), 6)
        self.player.lose()
        self.assertEqual(len(self.player.sequence), 7)
        self.assertEqual(self.player.sequence[-1], self.player.sequence[0]+self.player.sequence[-2])
        self.assertEqual(self.player.bet_amount, self.player.sequence[0]+self.player.sequence[-1])

    def tearDown(self):
        self.wheel = None
        self.table = None
        self.player = None         

if __name__ == '__main__':
    unittest.main()