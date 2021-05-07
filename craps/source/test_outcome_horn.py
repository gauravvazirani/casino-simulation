import unittest
import outcome
import throw

class TestOutcome(unittest.TestCase):

	def setUp(self):
		self.outcome1 =  outcome.OutcomeHorn('Horn',1)
		self.outcome2 = outcome.OutcomeHorn('Horn',1)
		self.throw1 = throw.Throw(1,1)
		self.throw2 = throw.Throw(1,2)
	
	def test_winAmount(self):
		self.assertEqual(self.outcome1.winAmount(4, self.throw1), 27)
		self.assertEqual(self.outcome2.winAmount(50, self.throw2), 150)

if __name__=='__main__':
	unittest.main()
			