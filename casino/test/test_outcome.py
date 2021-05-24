import unittest
from src import outcome
from src import throw 

class TestOutcome(unittest.TestCase):

	def setUp(self):
		self.outcome1 =  outcome.Outcome('Any Craps',2.5)
		self.outcome2 = outcome.Outcome('Hard 4',10)
		self.throw = throw.Throw(2,2)
	
	def test_winAmount(self):
		self.assertEqual(self.outcome1.winAmount(10),25)
		self.assertEqual(self.outcome2.winAmount(50, self.throw),500)

if __name__=='__main__':
	unittest.main()
			