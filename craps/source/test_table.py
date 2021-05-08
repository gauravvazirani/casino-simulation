import table
import bet
import unittest
import outcome
import invalid_bet_exception

class TestTable(unittest.TestCase):

    def setUp(self):
        self.table = table.Table(limit=500)
        self.bets = [
            bet.Bet(5, outcome.Outcome("Number 1",35)),
            bet.Bet(20, outcome.Outcome("Number 2",35)),
            bet.Bet(50, outcome.Outcome("Number 3",35)),
            bet.Bet(490, outcome.Outcome("Number 4",35))
        ]

    def test_placeBet(self):
        print("\nTesting placeBet")
        self.table.placeBet(self.bets[0])
        self.table.placeBet(self.bets[1])
        print(self.table)

    def test___str__(self):
        print("\nTesting __str__")
        self.table.placeBet(self.bets[2])
        self.table.placeBet(self.bets[3])

        print(self.table)   

    def test___repr__(self):
        self.table.placeBet(self.bets[2])
        self.table.placeBet(self.bets[3])
        print("\nTesting __repr__")
        print(self.table.__repr__())   

    def test_isValid(self):
        print("\nTesting isValid")
        for bet in self.bets:
            try:
                self.table.placeBet(bet)
                self.table.isValid()
                
            except invalid_bet_exception.InvalidBetException as e:
                print("Table has invalid set of bets:\n", self.table.__repr__())
                print("Please add valid bets")
                self.table.bets = []
    
    def tearDown(self):
        self.table = None
        self.bets = None

if __name__ == '__main__':
    unittest.main()
