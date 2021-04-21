import unittest
import bet
import outcome

class TestBet(unittest.TestCase):
    """
    Class to test behavior of Class Bet 
    """

    def setUp(self):
        self.bet = bet.Bet(10, outcome.Outcome('Number 0', 35))

    def test_winAmount(self):
        """
        Testing method winAmount, 
        should return amount one added with bet amount.
        """
        self.assertEqual(self.bet.winAmount(), 360)
        
    def test_loseAmount(self):
        """
        Testing loseAmount, 
        Amount lost is basically amount wagered.
        """
        self.assertEqual(self.bet.loseAmount(), 10)

    def test___str__(self):
        """
        string description of the form bet on amount
        """
        print(self.bet.__str__())
    
    def test___repr__(self):
        """
        string representation of object made
        """
        print(self.bet.__repr__())

    def tearDown(self):
        self.bet = None

if __name__ == '__main__':
    unittest.main()
