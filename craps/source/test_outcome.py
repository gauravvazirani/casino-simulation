import unittest
import outcome

class TestOutcome(unittest.TestCase):

	def test_winAmount(self):
		self.assertEqual(outcome.Outcome('Any Craps',2.5).winAmount(10),25)
		self.assertEqual(outcome.Outcome('Eleven',10).winAmount(15),150)
	
if __name__=='__main__':
	unittest.main()
			