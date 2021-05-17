import dice
import roulette_cancellation
import bet
import table
import unittest
import craps_game
import outcome
import craps_cancellation
import craps_game_state

class TestCancellation(unittest.TestCase):
    def setUp(self):
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  craps_game.CrapsGame(
            table=self.table, dice=self.dice)
        self.table.setGame(self.game)
        self.line = outcome.Outcome('Pass Line', 1)
        self.odds = outcome.Outcome('Pass Line Odds', 1)
        self.player = craps_cancellation.CrapsCancellation(
            table=self.table, line=self.line, odds=self.odds)
        self.player.setStake(1000)    
        self.bet = bet.Bet(outcome=self.odds, amount=10)

    def test_placeBets(self):
        self.game.state = craps_game_state.CrapsGamePointOn(point=5 ,game=self.game)
        self.assertEqual(len(self.table.bets), 0)
        self.assertEqual(self.player.stake, 1000)
        self.player.placeBets(2)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(self.player.stake, 993)

    def test_win(self):
        self.assertEqual(len(self.player.sequence), 6)
        if len(self.player.sequence)==1:
            self.bet.bet_amount = self.player.sequence[0]
        elif len(self.player.sequence)>1:
            self.bet.bet_amount = self.player.sequence[0] 
            + self.player.sequence[-1]
        self.player.win(self.bet)
        self.assertEqual(len(self.player.sequence), 4)
        self.assertEqual(len(self.player.sequence), 4)

    def test_lose(self):
        self.assertEqual(len(self.player.sequence), 6)
        self.player.lose()
        self.assertEqual(len(self.player.sequence), 7)
        self.assertEqual(
            self.player.sequence[-1], 
            self.player.sequence[0]+self.player.sequence[-2])

    def tearDown(self):
        self.wheel = None
        self.table = None
        self.player = None         

if __name__ == '__main__':
    unittest.main()
