import unittest
from src import outcome
from src import craps_onebetplayer
from src import table 
from src import bet1326_betting

class TestNochangeBetting(unittest.TestCase):
    def setUp(self):
        self.outcome = outcome.Outcome('Pass Line', 1) 
        self.strategy = bet1326_betting.Craps1326Betting(
            self.outcome
        )
        self.table = table.Table(5,1000) 
        self.player = craps_onebetplayer.OneBetPlayer(
          table = self.table,
          strategy = self.strategy  
        )

    def test_createBet(self):
        test_bet = self.strategy.createBet(self.player)
        self.assertEqual(test_bet.amount, 10)
        self.assertEqual(test_bet.outcome, self.outcome)

    def test_win(self):
        multiplier_map = {
            1:3,
            2:2,
            3:6,
            4:1
        }
        for num_wins in range(1,5):
            for index in range(1,num_wins+1):                
                self.strategy.win()
                self.assertEqual(
                    self.strategy.state.bet_multiple,
                    multiplier_map[index]
                )
                test_bet_win = self.strategy.createBet(self.player)
                self.assertEqual(
                    test_bet_win.amount,
                    multiplier_map[index]*self.strategy.bet_amount
                )
            self.strategy.lose()
            self.assertEqual(self.strategy.state.bet_multiple, 1)
            test_bet_lose = self.strategy.createBet(self.player)
            self.assertEqual(
                test_bet_lose.amount,
                self.strategy.bet_amount
            )

    def test_lose(self):
        self.strategy.lose()
        self.assertEqual(self.strategy.state.bet_multiple, 1)        
        test_bet = self.strategy.createBet(self.player)
        self.assertEqual(test_bet.amount, 10)
        self.assertEqual(self.strategy.bet_amount, 10)

    def tearDown(self):
        self.outcome = None
        self.strategy = None
        self.table = None
        self.player = None

if __name__ == '__main__':
    unittest.main()
