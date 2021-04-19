import unittest
import bin_builder
import wheel


def testFuncDecorator(func):
	def wrapper(*args, **kwargs):
		print(f"testing {func.__name__}")
		test_wheel = func(*args, **kwargs)
		print(f"whek status after calling {fun.__name__}")
		for index in range(38):
			priont(f"Bin {index}:", test_wheel.get(index))
			
			
Class TestBinBuilder(unittest.TestCase):
	"""
	Class for testing functionality of 
	bin builder
	"""
	def SetUp(self):
		"""
		set up data structure necessary at the begining of every test
		"""
		print("Set Up")
		self.builder = bin_builder.BinBuilder(wheel.Wheel())
		
	@testFuncDecorator
	def test_generateStraightBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateStraightBets().buildBins()



	@testFuncDecorator
	def test_generateSplitBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateSplitBets().buildBins()


	@testFuncDecorator
	def test_generateStreetBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateStreetBets().buildBins()


	@testFuncDecorator
	def test_generateCornerBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateCornerBets().buildBins()


	@testFuncDecorator
	def test_generateLineBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateLineBets().buildBins()


	@testFuncDecorator
	def test_generateDozenBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateDozenBets().buildBins()


	@testFuncDecorator
	def test_generateColumnBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateColumnBets().buildBins()


	@testFuncDecorator
	def test_generateEvenMoneyBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateEvenMoneyBets().buildBins()


	@testFuncDecorator
	def test_generateSpecialBet(self):
		"""
		method to test the functionality of generateStraight Bet
		"""
		return self.builder.generateSpecialBets().buildBins()


	def tearDown(self):
		"""
		Tear down data structure at the end of every test
		"""		
		print("Tear Down")
		self.builder = None
		
class TestWheelDirector(unittest.TestCase):
		"""
		Class to test functionality of Class WheelDirector
		"""	
		def setUp(self):
			self.Director = bin_builder.WheelDirector()
			
		@testFuncDecorator
		def test_construct(self):
			"""
			Method to test creation of a wheel using builder method
			"""
			return self.Director.construct(wheel.Wheel())
			
		def tearDown(self):
			self.Director = None
			
if __name__ == '__main__':
	unittest.main()
		
	
	
	





