import unittest
import bin_builder
import wheel
import inspect
fname = lambda: inspect.stack()[1][3] 
			
class TestBinBuilder(unittest.TestCase):
	"""
	Class for testing functionality of 
	bin builder
	"""

	def setUp(self):
		"""
		set up data structure necessary at the begining of every test
		"""
		self.builder = bin_builder.BinBuilder()

	def test_generateStraightBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateStraightBets().buildBins()

	def test_generateSplitBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateSplitBets().buildBins()

	def test_generateStreetBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateStreetBets().buildBins()

	def test_generateCornerBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateCornerBets().buildBins()

	def test_generateLineBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateLineBets().buildBins()

	def test_generateDozenBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateDozenBets().buildBins()

	def test_generateColumnBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateColumnBets().buildBins()

	def test_generateEvenMoneyBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateEvenMoneyBets().buildBins()

	def test_generateSpecialBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.wheel = self.builder.generateSpecialBets().buildBins()

	def tearDown(self):
		"""
		Tear down data structure at the end of every test
		"""		
		test_indices = (0,1,5,37) 
		for index in test_indices:
			print(f"index {index}", self.wheel.get(index))
		self.builder = None

class TestWheelDirector(unittest.TestCase):
	"""
	Class to test functionality of Class WheelDirector
	"""	
	def setUp(self):
		self.Director = bin_builder.WheelDirector()
		
	def test_construct(self):
		"""
		Method to test creation of a wheel using builder method
		"""
		print(f"testing {fname()}")
		self.wheel = self.Director.construct()
		
	def tearDown(self):
		test_indices = (0,1,5,37) 
		for index in test_indices:
			print(f"index {index}", self.wheel.get(index))
		self.Director = None
			

if __name__ == '__main__':
    unittest.main()

