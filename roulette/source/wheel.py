import random
import bin

class Wheel():
	"""
	Wheel contains the 38 bins present on a roulette wheel
	and a random number generator. Thus, It can select a bin at random,
	simulating the spin of a roulette wheel.
	"""
	def __init__(self):
		"""
		Creates a new wheel wth 38 empty bins.
		It will also create a new random number generator.
		"""
		self.bins = tuple(bin.Bin() for i in range(38))
		self.rng = random.Random()
		self.all_outcomes = dict()

	def addOutcome(self, number, outcome):
		"""
		Adds the given outcome to the bin with the given number.
		
		:param bin: (int)
		:param outcome: (Outcome)
		"""
		self.all_outcomes.update({outcome.name:outcome})
		self.bins[number].add(outcome)

	def getOutcome(self, name):
		"""
		Getter to fecth Outcome Object from the map of Outcomes
		
		:param name: (str)
		:return: (Outcome)
		"""
		return self.all_outcomes.get(name)
		
	def next(self):
		"""
		Generates a random number between 0 and 37 with replacement, and returns the randomly selected bin
		there by simulating a spin of the roulette wheel	
		
		:return: (Bin)
		"""
		return self.bins[self.rng.randint(0,37)] 
		
		
	def get(self, number):
		"""
		:param bin: (int)
		:return: (Bin)
		"""
		return self.bins[number]
	