import unittest
import craps_player
import bet 
import outcome
import table 

class TestCrapsPlayer(unittest.TestCase):

    def setUp(self):
        self.table = table.Table()
        self.player = craps_player.CrapsPlayer(self.table)
        self.outcome = outcome.Outcome('Pass Line',1)
        self.bet = bet.Bet(outcome=self.outcome, amount=10)

    def test_setRounds(self):
        self.assertEqual(self.player.rounds_to_go, 250)
        self.player.setRounds(100)
        self.assertEqual(self.player.rounds_to_go, 100)

    def test_setStake(self):
        self.assertEqual(self.player.stake, 10000)
        self.player.setStake(2000)
        self.assertEqual(self.player.stake, 2000)

    def test_playing(self):
        self.player.setRounds(10)
        self.player.setStake(20)
        self.table.bets=[]
        self.assertEqual(self.player.playing(), True)
        self.table.bets=[self.bet]
        self.assertEqual(self.player.playing(), True)
        self.player.setRounds(0)
        self.assertEqual(self.player.playing(), True)
        self.player.setStake(0)
        self.assertEqual(self.player.playing(), True)
        self.table.bets=[]
        self.assertEqual(self.player.playing(), False)

    def test_win(self):
        self.assertEqual(self.player.stake, 10000)
        self.player.win(self.bet)
        self.assertEqual(self.player.stake, 10020)

if __name__ == '__main__':
    unittest.main()
