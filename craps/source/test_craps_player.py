import unittest
import craps_player
import table 
import bet
import outcome
import dice
import craps_game

class TestCrapsPlayerPass(unittest.TestCase):

    def setUp(self):
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game = craps_game.CrapsGame(table=self.table, dice=self.dice)
        self.table.setGame(self.game)
        self.outcome = outcome.Outcome('Pass Line',1)
        self.odds = outcome.Outcome('Pass Line Odds',1)
        self.bet = bet.Bet(outcome=self.outcome, amount=10)
        self.player = craps_player.CrapsSimplePlayer(
            self.table, 
            line=self.outcome, 
            odds=self.odds
        )

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
