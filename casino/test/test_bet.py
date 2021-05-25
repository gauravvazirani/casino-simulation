import unittest
from src import bet
from src import outcome

class TestBet(unittest.TestCase):
    """
    Class to test behavior of Class Bet 
    """

    def setUp(self):
        self.bet = bet.Bet(10, outcome.Outcome('Number 0', 35), None)
        self.bet_commission_buy = bet.CommissionBet(20, outcome.Outcome('Buy',2), None)
        self.bet_commission_lay = bet.CommissionBet(30, outcome.Outcome('Lay',2/3), None)
    
    def test_winAmount(self):
        """
        Testing method winAmount, 
        should return amount won added with bet amount.
        """
        self.assertEqual(self.bet.winAmount(), 360)
        self.assertEqual(self.bet_commission_buy.winAmount(), 60)
        self.assertEqual(self.bet_commission_lay.winAmount(), 50)

    def test_price(self):
        """
        Testing method price, 
        should return commission added with bet amount.
        """
        self.assertEqual(self.bet.price(), 10)
        self.assertEqual(self.bet_commission_buy.price(), 21)
        self.assertEqual(self.bet_commission_lay.price(), 31)

    def test_loseAmount(self):
        """
        Testing loseAmount, 
        Amount lost is basically amount wagered.
        """
        self.assertEqual(self.bet.loseAmount(), 10)
        self.assertEqual(self.bet_commission_buy.loseAmount(), 20)
        self.assertEqual(self.bet_commission_lay.loseAmount(), 30)

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
        self.bet_commission_buy = None
        self.bet_commission_lay = None

if __name__ == '__main__':
    unittest.main()
