import unittest
import wheel
import random
import outcome
import bin
import bin_builder
from unittest.mock import Mock, MagicMock

class TestWheel(unittest.TestCase):
	"""
	Test class for performing unit test of class wheel
	"""
	
	def setUp(self):
		"""
		Sets seed for random number generator of the wheel
		Create outcomes required to test addition of outcomes
		Inititialize a bin to test get method
		"""
		self.wheel = bin_builder.WheelDirector.construct()
		# self.wheel.rng.seed(1)
		self.wheel.rng = Mock()
		self.wheel.rng.randint = Mock(return_value=1)
		self.outcome_test = outcome.Outcome("00-test",35)
		
		
	def test_addOutcome(self):
		"""
		method to test addition of outcomes in a bin object
		at a particular location of the wheel
		"""
		print("\naddOutcome")
		print("bin contents before addition of outcome:")
		print(f"bin 37:",self.wheel.get(37))
		self.wheel.addOutcome(37,self.outcome_test)
		print("bin contents after addition of outcome:")
		print(f"bin 37:",self.wheel.get(37))
		
	def test_next(self):
		"""
		method to test the randomness of the wheel spin
		compares the wheel random number generator to an object
		from random.Random class
		"""
		print("\nnext")
		# test_random = random.Random()
		# test_random.seed(1)
		# print([(self.wheel.bins[test_random.randint(0,37)]) for i in range(10)])
		self.assertEqual(self.wheel.bins[1],self.wheel.next())
		self.wheel.rng.randint.assert_called_with(0,37)

	def test_get(self):
		"""
		method to test the get method
		gets object at specified position of th wheel and prints the returned object
		"""
		print("\nget")
		print("bin 0:", self.wheel.get(0))
		self.assertEqual(self.wheel.get(0),bin.Bin([outcome.Outcome("Number 0",35),outcome.Outcome("00-0-1-2-3",6)]))

	def test_getOutcome(self):
		"""
		testing getOutcome
		should return outcome object from all_outcomes 
		in case the name exists and None otherwise  
		"""
		print("\ngetOutcome")
		self.assertEqual(self.wheel.getOutcome('Number 0'), outcome.Outcome('Number 0', 35))
		self.assertEqual(self.wheel.getOutcome('Number 85'), None)

	def tearDown(self):
		self.wheel = None
	
if __name__=='__main__':
	unittest.main()
	