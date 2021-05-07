import outcome
from abc import abstractmethod,ABCMeta
import throw
import dice

class CrapsGame():
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
	def buildThrows():
		"""
		Returns wheel built after all the bins
		"""
		

class ThrowBuilder(IBuilder):
    """
    Class responsible for setting the wheel with the
    correct placement of outcomes on appropriate bins
    """

    def __init__(self):
        self.dice = dice.Dice()
        for d1 in range(1,7):
            for d2 in range(1,7):
                self.dice.addThrow(throw.Throw(d1,d2))
        
    def generateStraightThrows(self):
        for d1 in range(1,7):
            for d2 in range(1,7):
                if d1 + d2 in (2,3,7,11,12):
                    self.dice.getThrow(d1,d2).add(
                        outcome.Outcome(
                        f'Number {d1+d2}', CrapsGame.straight[d1+d2]
                        )
                    )
        return self

    def generateFieldThrows(self):
        oc = outcome.Outcome('Field', CrapsGame.field)
        for d1 in range(1,7):
            for d2 in range(1,7):
                if d1 + d2 in (2,3,4,9,10,11,12):
                    self.dice.getThrow(d1,d2).add(oc)
        return self

    def generateHornThrows(self):
        oc = outcome.Outcome('Horn', CrapsGame.horn)
        for d1 in range(1,7):
            for d2 in range(1,7):
                if d1 + d2 in (2,3,11,12):
                    self.dice.getThrow(d1,d2).add(oc)
        return self

    def generateAnyCrapsThrows(self):
        oc = outcome.Outcome('Any Craps', CrapsGame.anyCraps)
        for d1 in range(1,7):
            for d2 in range(1,7):
                if d1 + d2 in (2,3,12):
                    self.dice.getThrow(d1,d2).add(oc)
        return self	

    def buildThrows(self):
        return self.dice

	
class DiceDirector():
	"""
	The director class for the dice, building a complex representation
	"""

	@staticmethod
	def construct():
		"""
		Constructs and returns the dice with all the outcomes
		"""
		return ThrowBuilder()\
			.generateStraightThrows()\
			.generateFieldThrows()\
			.generateHornThrows()\
			.generateAnyCrapsThrows()\
			.buildThrows()
			