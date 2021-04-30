import unittest
import player1326
import player1326_state
import table 
import bin_builder
from unittest.mock import Mock
import bet

class TestPlayer1326_test(unittest.TestCase):

    def setUp(self):
        self.table = table.Table()      
        wheel = bin_builder.WheelDirector().construct() 
        self.wheel = wheel
        self.player = player1326.Player1326(wheel=self.wheel, table=self.table, initial_bet_amount=10)
        self.bet = bet.Bet(outcome=self.wheel.all_outcomes.get('Black'), amount=10)
        

    def test_placeBets(self):
        multiplier_map = {
            1:3,
            2:2,
            3:6,
            4:1
        }
        self.assertEqual(len(self.table.bets), 0)
        self.player.placeBets()
        self.assertEqual(self.table.bets[0].amount, 10)      
        for num_wins in range(1,5):
            for index in range(1,num_wins+1):                
                self.player.win(self.bet)
                self.player.placeBets()
                self.assertEqual(self.table.bets[-1].amount, multiplier_map[index]*10)
            self.player.lose(self.bet)
            self.player.placeBets()            
            self.assertEqual(self.table.bets[-1].amount, 10)

    def test_win(self):
        self.assertEqual(self.player.state.bet_multiple, 1)
        self.player.placeBets()
        self.player.win(self.bet)
        self.assertEqual(self.player.state.bet_multiple, 3)

    def test_lose(self):
        self.assertEqual(self.player.state.bet_multiple, 1)
        self.player.placeBets()
        self.player.lose(self.bet)
        self.assertEqual(self.player.state.bet_multiple, 1)

    def tearDown(self):
        self.table = None
        self.wheel = None 
        self.player = None

if __name__ == '__main__':
    unittest.main()