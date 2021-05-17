import unittest
import roulette1326
import table 
import wheel
from unittest.mock import Mock
import bet
import roulette_game

class TestPlayer1326(unittest.TestCase):

    def setUp(self):
        self.wheel = wheel.Wheel()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  roulette_game.RouletteGame(table=self.table, wheel=self.wheel)
        self.table.setGame(self.game)
        self.player = roulette1326.Roulette1326(wheel=self.wheel, table=self.table)
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
            self.player.lose()
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
        self.player.lose()
        self.assertEqual(self.player.state.bet_multiple, 1)

    def tearDown(self):
        self.table = None
        self.wheel = None 
        self.player = None

if __name__ == '__main__':
    unittest.main()