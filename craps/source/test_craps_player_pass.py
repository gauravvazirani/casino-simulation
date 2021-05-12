import unittest
import craps_player_pass
import table 
import bet
import outcome

class TestCrapsPlayerPass(unittest.TestCase):

    def setUp(self):
        self.table = table.Table()
        self.player = craps_player_pass.CrapsPlayerPass(self.table)
        self.outcome = outcome.Outcome('Pass Line',1)
        
    def test_placeBets(self):
        self.player.setStake(25)
        self.player.setRounds(5)
        self.player.bet_amount=10
        self.table.bets = []
        self.player.placeBets(point=0)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.table.bets[0].outcome, self.outcome)        
        self.assertEqual(self.player.stake, 15)        

        self.player.placeBets(point=0)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.table.bets[0].outcome,self.outcome)        
        self.assertEqual(self.player.stake, 15)        

        self.table.bets = []
        self.player.bet_amount = 20
        self.player.placeBets(point=0)
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 15)        

        self.player.bet_amount=10
        self.player.setRounds(0)
        self.player.placeBets(point=0)
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 15)        

        self.player.placeBets(point=1)
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 15)        



if __name__ == '__main__':
    unittest.main()
