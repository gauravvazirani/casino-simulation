from outcome import Outcome
from abc import abstractmethod,ABCMeta
import wheel

class RouletteGame():
	"""
	A class representing the odds of various bets in roulette
	"""
	StraightBet = 35
	SplitBet = 17
	StreetBet = 11 
	CornerBet = 8 
	LineBet = 5
	DozenBet = 2
	ColumnBet = 2
	EvenMoneyBet = 1
	
	
class IBuilder(metaclass=ABCMeta):
	
	@staticmethod
	@abstractmethod
	def generateStraightBets():
		"""
		Adds outcome for straight bets, assigns to bins at respective positions on the wheel
		Each number is an outcome with odds 35:1
		"""

	@staticmethod
	@abstractmethod
	def generateSplitBets():
		"""
		Adds outcome for split bets, assigns to bins at respective positions on the wheel
		Each number is adjacent to 2,3 or 4 numbers 
		Generate Split bet outcomes on the basis of the number of sides shared
		Odds are 17:1
		"""

	@staticmethod
	@abstractmethod
	def generateStreetBets():
		"""
		Adds outcome for street bets, 
		Set of every 3 numbers on every row of the table.
		Total 12 streets with odds of 11:1
		"""

	@staticmethod
	@abstractmethod
	def generateCornerBets():
		"""
		Adds outcome for Corner bets, 
		Each number is a member of 1,2 or 4 corner bets.
		Odds are 8:1
		"""

	@staticmethod
	@abstractmethod
	def generateLineBets():
		"""
		Adds outcomes for line bets
		6 consecutive numbers comprise a line 
		Each number is a member of 1 or 2 lines
		Odds are 5:1 
		"""

	@staticmethod
	@abstractmethod
	def generateDozenBets():
		"""
		Adds outcome for Dozen bets, 
		numbers are divided into 3 dozens
	    Each number is an outcome with odds 2:1
		"""


	@staticmethod
	@abstractmethod
	def generateColumnBets():
		"""
		Adds outcome for Column bets, 
		Each number is a member of 1 of 3 columns
		Generate outcomes and assign to bins based on column membership
		Odds are 2:1
		"""


	@staticmethod
	@abstractmethod
	def generateEvenMoneyBets():
		"""
		Adds outcome for even money bets, 
		These include high, low, even, odd, red, black.
		Odds are 1:1
		"""
		
	@staticmethod
	@abstractmethod
	def generateSpecialBets():
		"""
		Adds outcome for bins 0,00
		"""
		
	@staticmethod
	@abstractmethod
	def buildBins():
		"""
		Returns wheel built after all the bins
		"""
		
	
class BinBuilder(IBuilder):
	"""
	Class responsible for setting the wheel with the
	correct placement of outcomes on appropriate bins
	"""

	def __init__(self):
		self.wheel = wheel.Wheel()

	def generateStraightBets(self):
		for num in range(1,37):
			self.wheel.addOutcome(
				num,
				Outcome('Number '+str(num),
					RouletteGame.StraightBet)
			)
		self.wheel.addOutcome(0,Outcome('Number 0', RouletteGame.StraightBet))
		self.wheel.addOutcome(00,Outcome('Number 00', RouletteGame.StraightBet))
		return self
	

	def generateSplitBets(self):
		for rownum in range(12):
			for colnum in range(1,3):
				idx_left = 3*rownum+colnum
				self.wheel.addOutcome(
					idx_left,
					Outcome(f"Split {idx_left}, {idx_left+1}",
						RouletteGame.SplitBet
					)
				)
				self.wheel.addOutcome(
					idx_left+1,
					Outcome(f"Split {idx_left}, {idx_left+1}",
						RouletteGame.SplitBet
					)
				)
		for rownum in range(11):
			for colnum in range(1,4):
				idx_down = 3*rownum+colnum
				self.wheel.addOutcome(
					idx_down,
					Outcome(f"Split {idx_down},{idx_down+3}",
						RouletteGame.SplitBet
					)
				)	
				self.wheel.addOutcome(
					idx_down+3,
					Outcome(f"Split {idx_down},{idx_down+3}",
						RouletteGame.SplitBet
					)
				)
		return self
	
	def generateStreetBets(self):
		for rownum in range(12):
			sname = "Street "+",".join([str(3*rownum+colnum) for colnum in range(1,4)])
			oc = Outcome(sname, RouletteGame.StreetBet)
			for colnum in range(1,4):
				self.wheel.addOutcome(3*rownum+colnum,oc)
		return self
	
	def generateLineBets(self):
		for rownum in range(11):
			oc = Outcome(
				"Line " + str(rownum+1),
				RouletteGame.LineBet
			) 
			for colnum in range(1,7):
				self.wheel.addOutcome(3*rownum+colnum,oc)
		return self
	
	def generateCornerBets(self):
		for rownum in range(11):
			for colnum in range(1,3):
				idx_ul = 3*rownum+colnum
				idx_ur = idx_ul+1
				idx_ll = idx_ul+3
				idx_lr = idx_ll+1
				for idx in (idx_ul,idx_ur,idx_ll,idx_lr):
					self.wheel.addOutcome(
						idx,
						Outcome("Corner "+str(idx_ul),
							RouletteGame.CornerBet)
					) 
		return self


	def generateDozenBets(self):
		for idx_dozen in range(3):
			for rownum in range(1,13):
				self.wheel.addOutcome(
					12*idx_dozen+rownum,
					Outcome(
						f"Dozen {idx_dozen+1}",
						RouletteGame.DozenBet
					)
				)	
		return self
			
	def generateColumnBets(self):
		for colnum in range(1,4):
			oc = Outcome(
				"Column"+str(colnum),
				RouletteGame.ColumnBet
			)
			for rownum in range(12):
				self.wheel.addOutcome(
					3*rownum+colnum,
					oc
				)
		return self
	
	def generateEvenMoneyBets(self):

		red_nums = set([1, 3, 5, 7, 9,
			12, 14, 16, 18, 19,
			21, 23, 25, 27, 30,
			32, 34, 36])

		for binnum in range(1,37):
			if 1 <= binnum <= 18:
				self.wheel.addOutcome(
					binnum,
					Outcome("Low",
						RouletteGame.EvenMoneyBet
					)
				)
			else:
				self.wheel.addOutcome(
					binnum,
					Outcome("High",
						RouletteGame.EvenMoneyBet						
					)
				) 

			if binnum%2==0:
				self.wheel.addOutcome(
					binnum,
					Outcome("Even",
						RouletteGame.EvenMoneyBet
					)
				)
			else:
				self.wheel.addOutcome(
					binnum,
					Outcome("Odd",
						RouletteGame.EvenMoneyBet
					)
				)
				
			if binnum in red_nums:
				self.wheel.addOutcome(
					binnum,
					Outcome("Red",
						RouletteGame.EvenMoneyBet				
					)
				)		
			else:
				self.wheel.addOutcome(
					binnum,
					Outcome("Black",
						RouletteGame.EvenMoneyBet				
					)
				)		
		return self

	def generateSpecialBets(self):
		self.wheel.addOutcome(0,Outcome('00-0-1-2-3',6))
		self.wheel.addOutcome(37,Outcome('00-0-1-2-3',6))
		return self
	
	def buildBins(self):
		return self.wheel
	
	
	
class WheelDirector():
	"""
	The director class for a wheel, building a complex representation
	"""

	@staticmethod
	def construct():
		"""
		Constructs and returns the wheel with all the outcomes
		"""
		return BinBuilder()\
			.generateStraightBets()\
			.generateSplitBets()\
			.generateStreetBets()\
			.generateLineBets()\
			.generateColumnBets()\
			.generateCornerBets()\
			.generateDozenBets()\
			.generateSpecialBets()\
			.buildBins()
			
