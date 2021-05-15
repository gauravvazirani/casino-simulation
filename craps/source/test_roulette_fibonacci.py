import wheel
import roulette_fibonacci
import bet
import table
import unittest

class TestFibonacci(unittest.TestCase):    
    def setUp(self):
        self.wheel = wheel.Wheel()
        self.table = table.Table(minimum=1, maximum=1000)
        self.player = roulette_fibonacci.RouletteFibonacci(table=self.table, wheel=self.wheel)
        
    def test_placeBets(self):
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 1000)
        self.player.placeBets()
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.player.stake, 999)

    def test_win(self):
        self.assertEqual(self.player.current, 1)
        self.assertEqual(self.player.previous, 0)
        self.player.win(bet.Bet(outcome=self.wheel.all_outcomes.get('Black'), amount=self.player.current))
        self.assertEqual(self.player.current, 1)
        self.assertEqual(self.player.previous, 0)

    def test_lose(self):
        self.assertEqual(self.player.current, 1)
        self.assertEqual(self.player.previous, 0)
        self.player.lose()
        self.assertEqual(self.player.current, 1)
        self.assertEqual(self.player.previous, 1)

    def tearDown(self):
        self.wheel = None
        self.table = None
        self.player = None         

if __name__ == '__main__':
    unittest.main()