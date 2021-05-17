from unittest.mock import Mock
import unittest
import craps1326
import table
import wheel
import bet
import craps_game
import dice
import outcome
import craps_game_state

class TestPlayer1326(unittest.TestCase):

    def setUp(self):
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  craps_game.CrapsGame(
            table=self.table, dice=self.dice)
        self.table.setGame(self.game)
        self.line = outcome.Outcome('Pass Line', 1)
        self.odds = outcome.Outcome('Pass Line Odds', 1)
        self.player = craps1326.Craps1326(
            table=self.table, line=self.line, odds=self.odds)    
        self.bet = bet.Bet(outcome=self.odds, amount=10)
   
    def test_placeBets(self):
        multiplier_map = {
            1:3,
            2:2,
            3:6,
            4:1
        }
        self.game.state = craps_game_state.CrapsGamePointOn(point=5 ,game=self.game)
        self.assertEqual(len(self.table.bets), 0)
        self.player.placeBets(5)
        self.assertEqual(self.table.bets[0].amount, 10)      
        for num_wins in range(1,5):
            for index in range(1,num_wins+1):                
                self.table.clear()
                self.player.win(self.bet)
                self.player.placeBets(5)
                self.assertEqual(self.table.bets[-1].amount, multiplier_map[index]*10)
            self.player.lose()
            self.table.clear()
            self.player.placeBets(5)            
            self.assertEqual(self.table.bets[-1].amount, 10)

    def test_win(self):
        self.assertEqual(self.player.state.bet_multiple, 1)
        self.player.win(self.bet)
        self.assertEqual(self.player.state.bet_multiple, 3)
        self.player.win(self.bet)
        self.assertEqual(self.player.state.bet_multiple, 2)
        self.player.win(self.bet)
        self.assertEqual(self.player.state.bet_multiple, 6)

    def test_lose(self):
        self.assertEqual(self.player.state.bet_multiple, 1)
        self.player.lose()
        self.assertEqual(self.player.state.bet_multiple, 1)

    def tearDown(self):
        self.table = None
        self.wheel = None 
        self.player = None

if __name__ == '__main__':
    unittest.main()