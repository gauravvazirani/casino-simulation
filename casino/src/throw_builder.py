from . import outcome
from abc import abstractmethod,ABCMeta
from . import throw


class CrapsGameOdds():
	"""
	A class representing the odds of various bets in craps
	"""
	straight = {
        2:31,
        3:16,
        7:5,
        11:16,
        12:31
    }
	field = 1.25
	horn = 3.75
	anyCraps = 8
	hardway = {
		2:1,
		4:2,
		6:3,
		8:3,
		10:4
	}
	passLine = 1
	dontPassLine = 1
	comeLine = 1
	dontComeLine = 1
	passLineOdds = 1
	dontPassLineOdds = 1
	comeLineOdds = 1
	dontComeLineOdds = 1

class IBuilder(metaclass=ABCMeta):
	
	@staticmethod
	@abstractmethod
	def generateStraightThrows():
		"""
		Adds outcome for straight throws, 
  		Each number is an outcome with odds 1:1
		"""

	@staticmethod
	@abstractmethod
	def generateFieldThrows():
		"""
		Adds outcome for field throws,
		Odds are 17:1
        In case of field outcome, if sum of the dice is 2 or 12 then the 
        odds are 2:1 otherwise its 1:1
		"""

	@staticmethod
	@abstractmethod
	def generateHornThrows():
		"""
		Adds outcome for Horn throws, 
        In case of horn outcome, if sum of the dice is 2 or 12 then the 
 	    odds are 27:4 otherwise its 3:1
		"""

	@staticmethod
	@abstractmethod
	def generateAnyCrapsThrows():
		"""
		Adds outcome for Any Craps throws, 
		"""

	@staticmethod
	@abstractmethod
	def generateHardwayThrows():
		"""
		Adds outcome for Harway throws, 
		"""

	@staticmethod
	@abstractmethod
	def buildThrows():
		"""
		Returns wheel built after all the bins
		"""
		

class ThrowBuilder(IBuilder):
	"""
	Class responsible for setting the wheel with the
	correct placement of outcomes on appropriate bins
	"""
	def __init__(self, dice):
		self.dice = dice
		for d1 in range(1,7):
			for d2 in range(1,7):
				s = d1 + d2
				if s in (4,5,6,8,9,10):
					self.dice.addThrow(throw.PointThrow(d1,d2))
				elif s == 7:
					self.dice.addThrow(throw.NaturalThrow(d1,d2))
				elif s in (2,3,12):
					self.dice.addThrow(throw.CrapsThrow(d1,d2))
				elif s == 11:
					self.dice.addThrow(throw.ElevenThrow(d1,d2))

		oc_dict = {
			'Field': CrapsGameOdds.field,
			'Horn': CrapsGameOdds.horn,
			'AnyCraps': CrapsGameOdds.anyCraps,
			'Pass Line': CrapsGameOdds.passLine,
			'Dont Pass Line': CrapsGameOdds.dontPassLine,
			'Pass Line Odds': CrapsGameOdds.passLineOdds,
			'Dont Pass Line Odds': CrapsGameOdds.dontPassLineOdds,
			'Come Line': CrapsGameOdds.comeLine,
			'Dont Come Line': CrapsGameOdds.dontComeLine,
			'Come Line Odds': CrapsGameOdds.comeLineOdds,
			'Dont Come Line Odds': CrapsGameOdds.dontComeLineOdds
		}
		for name, odds in oc_dict.items():
			self.dice.all_outcomes.update({
				name: outcome.Outcome(name, odds)
			})

	def generateStraightThrows(self):
		for d1 in range(1,7):
			for d2 in range(1,7):
				if d1 + d2 in (2,3,7,11,12):
					oc = outcome.Outcome(
						f'Number {d1+d2}', CrapsGameOdds.straight[d1+d2]
						)	
					self.dice.getThrow(d1,d2).win_1roll.add(oc)
					self.dice.all_outcomes.update({oc.name:oc})
		return self

	def generateFieldThrows(self):
		oc = self.dice.all_outcomes.get('Field')
		for d1 in range(1,7):
			for d2 in range(1,7):
				if d1 + d2 in (2,3,4,9,10,11,12):
					self.dice.getThrow(d1,d2).win_1roll.add(oc)
		return self

	def generateHornThrows(self):
		oc = self.dice.all_outcomes.get('Horn')
		for d1 in range(1,7):
			for d2 in range(1,7):
				if d1 + d2 in (2,3,11,12):
					self.dice.getThrow(d1,d2).win_1roll.add(oc)
		return self

	def generateAnyCrapsThrows(self):
		oc = self.dice.all_outcomes.get('Any Craps')
		for d1 in range(1,7):
			for d2 in range(1,7):
				if d1 + d2 in (2,3,12):
					self.dice.getThrow(d1,d2).win_1roll.add(oc)
		return self	

	def generateHardwayThrows(self):		
		for d1 in range(1,7):
			for d2 in range(1,7):
				if d1 + d2 in (4,6,8,10):
					oc = outcome.Outcome(f'Hardway {d1+d2}', CrapsGameOdds.hardway[d1+d2])
					self.dice.all_outcomes.update({oc.name:oc})
					if self.dice.getThrow(d1,d2).hard():
						self.dice.getThrow(d1,d2).addHardways(
							[oc], []
							)
					else:
						self.dice.getThrow(d1,d2).addHardways(
							[], [oc]
							)
		return self

	def buildThrows(self):
		return


class DiceDirector():
	"""
	The director class for the dice, building a complex representation
	"""

	@staticmethod
	def construct(dice):
		"""
		Constructs and returns the dice with all the outcomes
		"""
		return ThrowBuilder(dice)\
			.generateStraightThrows()\
			.generateFieldThrows()\
			.generateHornThrows()\
			.generateAnyCrapsThrows()\
			.generateHardwayThrows()\
			.buildThrows()
			