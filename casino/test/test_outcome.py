import unittest
from src import outcome
from src import throw 

class TestOutcome(unittest.TestCase):

	def setUp(self):
		self.outcome1 =  outcome.Outcome('Any Craps',2.5)
	
	def test_winAmount(self):
		self.assertEqual(self.outcome1.winAmount(10),25)

if __name__=='__main__':
	unittest.main()
			