import unittest
import craps_player_martingale
import table 
import bet
import outcome

class TestCrapsPlayerMartingale(unittest.TestCase):

    def setUp(self):
        self.table = table.Table()
        self.player = craps_player_martingale.CrapsPlayerMartingale(self.table)
        self.outcome = outcome.Outcome('Pass Line', 1)
        self.odds_outcome = outcome.Outcome('Pass Line Odds', 1)
        self.bet = bet.Bet(outcome=self.outcome, amount=10)        
   
    def test_placeBets(self):
        self.player.setStake(25)
        self.player.setRounds(5)
        self.player.bet_amount=10
        self.table.bets = []
        self.player.placeBets(pointval=0)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.table.bets[0].outcome, self.outcome)        
        self.assertEqual(self.player.stake, 15)        

        self.player.placeBets(pointval=0)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.table.bets[0].outcome,self.outcome)        
        self.assertEqual(self.player.stake, 15)        

        self.table.bets = []
        self.player.bet_amount = 20
        self.player.placeBets(pointval=0)
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 15)        

        self.player.bet_amount=10
        self.player.setRounds(0)
        self.player.placeBets(pointval=0)
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 15)        

        self.player.bet_amount=10
        self.player.bet_multiple=2
        self.player.setRounds(10)
        self.player.setStake(25)
        self.player.placeBets(pointval=1)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.player.stake, 5)        
        self.assertEqual(self.table.bets[0].outcome,self.odds_outcome)        
        
        self.player.bet_amount=10
        self.player.bet_multiple=2
        self.player.setStake(15)
        self.table.bets = []
        self.player.placeBets(pointval=1)
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 15)        

    def test_win(self):
        self.player.setStake(30)
        self.assertEqual(self.player.loss_count, 0)
        self.assertEqual(self.player.bet_multiple, 1)        
        self.player.win(self.bet)
        self.assertEqual(self.player.stake, 50)
        self.assertEqual(self.player.loss_count, 0)
        self.assertEqual(self.player.bet_multiple, 1)

    def test_lose(self):
        self.player.setStake(30)
        self.assertEqual(self.player.loss_count, 0)
        self.assertEqual(self.player.bet_multiple, 1)        
        self.player.lose(self.bet)
        self.assertEqual(self.player.stake, 30)
        self.assertEqual(self.player.loss_count, 1)
        self.assertEqual(self.player.bet_multiple, 2)

if __name__ == '__main__':
    unittest.main()
