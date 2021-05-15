import table
import bet
import unittest
import outcome
import invalid_bet_exception
import craps_game

class TestCrapsTable(unittest.TestCase):

    def setUp(self):
        self.table = table.Table(minimum=1, maximum=1000)
        self.game = craps_game.CrapsGame()
        self.table.setGame(self.game)
        self.bets = [
            bet.Bet(5, outcome.Outcome("Pass", 2)),
            bet.Bet(10, outcome.Outcome("Any Craps", 31)),
            bet.Bet(50, outcome.Outcome("Odds on Come", 16)),
            bet.Bet(490, outcome.Outcome("Don't Pass", 2))
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
        self.assertEqual(self.table.isValid(self.bets[0]), True)
        self.assertEqual(self.table.isValid(self.bets[1]), False)
        self.assertEqual(self.table.isValid(self.bets[2]), False)
        self.assertEqual(self.table.isValid(self.bets[3]), True)

    def test_allValid(self):
        print("\nTesting allValid")
        test_outcome = [True, False, False, False]
        for index in range(4):
            for _ in self.bets:
                try:
                    self.table.placeBet(self.bets[index])
                    self.assertEqual(
                        self.table.allValid(),
                        test_outcome[index]
                    )                
                except invalid_bet_exception.InvalidBetException as e:
                    print("Table limit exceeded:\n", self.table.__repr__())
                    self.table.bets = []
    
    def tearDown(self):
        self.table = None
        self.bets = None

if __name__ == '__main__':
    unittest.main()
