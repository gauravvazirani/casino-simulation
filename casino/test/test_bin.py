import unittest
from src import bin
from src import outcome

class TestBin(unittest.TestCase):
	"""
	Class to test creation of a bin object
	"""
	
	def test_bin(self):
		"""
		method that creates a set of outcomes associated to a couple of bins
		initializes couple of bins to test creation of bin using the outcomes
		"""
		outcome1 = outcome.Outcome("0",35)
		outcome2 = outcome.Outcome("00",35)
		outcome3 = outcome.Outcome("0-00-1-2-3",6)
		outcomes_zero = [
			outcome1,
			outcome3
		]
		outcomes_double_zero = [
			outcome2,
			outcome3
		]
		zero = bin.Bin(outcomes_zero)
		double_zero = bin.Bin(outcomes_double_zero)
		print("created bin 0 with following outcomes",zero)
		print("created bin 00 with following outcomes",double_zero)
		
if __name__=='__main__':
	unittest.main()
		 
	
	