import unittest
from src import table
from src import bet
from src import outcome
from src import invalid_bet_exception
from src import craps_game
from src import dice

class TestCrapsTable(unittest.TestCase):

    def setUp(self):
        self.table = table.Table(minimum=1, maximum=450)
        self.dice = dice.Dice()
        self.game = craps_game.CrapsGame(self.dice,self.table)
        self.bets = [
            bet.Bet(5, outcome.Outcome("Pass Line", 1)),
            bet.Bet(10, outcome.Outcome("Any Craps", 31)),
            bet.Bet(50, outcome.Outcome("Odds on Come", 16)),
            bet.Bet(490, outcome.Outcome("Dont Pass Line", 2))
        ]

    def test_placeBet(self):
        print("\nTesting placeBet")
        self.table.placeBet(self.bets[0],self.game)
        self.table.placeBet(self.bets[3],self.game)
        print(self.table)

    def test___str__(self):
        print("\nTesting __str__")
        self.table.placeBet(self.bets[0],self.game)
        self.table.placeBet(self.bets[3],self.game)
        print(self.table)   

    def test___repr__(self):
        self.table.placeBet(self.bets[0],self.game)
        self.table.placeBet(self.bets[3],self.game)
        print("\nTesting __repr__")
        print(self.table.__repr__())   


    def test_allValid(self):
        print("\nTesting allValid")
        try:
            self.table.placeBet(self.bets[0],self.game)
            self.table.allValid()
            print("Placed Bet Number 1")
            self.assertEqual(len(self.table.bets),1)
            self.table.placeBet(self.bets[3],self.game)
            self.table.allValid()
            print("Placed Bet Number 2")
        except invalid_bet_exception.InvalidBetException as e:
            print("Table limit exceeded:\n", self.table.__repr__())
            self.assertEqual(len(self.table.bets),2)
            self.table.bets = []
    
    def tearDown(self):
        self.table = None
        self.bets = None

if __name__ == '__main__':
    unittest.main()
