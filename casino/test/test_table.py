import unittest
from src import wheel
from src import table
from src import bet
from src import outcome
from src import invalid_bet_exception
from src import roulette_game

class TestTable(unittest.TestCase):

    def setUp(self):
        self.wheel = wheel.Wheel()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  roulette_game.RouletteGame(table=self.table, wheel=self.wheel)
        self.bets = [
            bet.Bet(5, outcome.Outcome("Number 1",35)),
            bet.Bet(20, outcome.Outcome("Number 2",35)),
            bet.Bet(50, outcome.Outcome("Number 3",35)),
            bet.Bet(490, outcome.Outcome("Number 4",35))
        ]

    def test_placeBet(self):
        print("\nTesting placeBet")
        self.table.placeBet(self.bets[0],self.game)
        self.table.placeBet(self.bets[1],self.game)
        print(self.table)

    def test___str__(self):
        print("\nTesting __str__")
        self.table.placeBet(self.bets[2],self.game)
        self.table.placeBet(self.bets[3],self.game)
        print(self.table)   

    def test___repr__(self):
        self.table.placeBet(self.bets[2],self.game)
        self.table.placeBet(self.bets[3],self.game)
        print("\nTesting __repr__")
        print(self.table.__repr__())   
    
    def tearDown(self):
        self.table = None
        self.bets = None

if __name__ == '__main__':
    unittest.main()
