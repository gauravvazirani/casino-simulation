import unittest
from src import bin_builder
from src import wheel
from src import bin
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
		self.wheel = wheel.Wheel()
		self.wheel.bins = tuple(bin.Bin() for i in range(38))
		self.builder = bin_builder.BinBuilder(self.wheel)

	def test_generateStraightBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateStraightBets().buildBins()

	def test_generateSplitBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateSplitBets().buildBins()

	def test_generateStreetBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateStreetBets().buildBins()

	def test_generateCornerBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateCornerBets().buildBins()

	def test_generateLineBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateLineBets().buildBins()

	def test_generateDozenBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateDozenBets().buildBins()

	def test_generateColumnBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateColumnBets().buildBins()

	def test_generateEvenMoneyBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateEvenMoneyBets().buildBins()

	def test_generateSpecialBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		print(f"testing {fname()}")
		self.builder.generateSpecialBets().buildBins()

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
		self.wheel = wheel.Wheel()
		self.wheel.bins = tuple(bin.Bin() for i in range(38))
		self.Director = bin_builder.WheelDirector()
		
	def test_construct(self):
		"""
		Method to test creation of a wheel using builder method
		"""
		print(f"testing {fname()}")
		self.Director.construct(self.wheel)
		
	def tearDown(self):
		test_indices = (0,1,5,37) 
		for index in test_indices:
			print(f"index {index}", self.wheel.get(index))
		self.Director = None
			

if __name__ == '__main__':
    unittest.main()

