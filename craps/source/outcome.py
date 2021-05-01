from fractions import Fraction

class Outcome():
	"""
	Defines an outcome of a game
	"""
	def __init__(self, name, odds):
		"""
		instantiates an outcome from its name and the odds
		
		:param name:
		:type string:
		:param odds:
		:type integer: 
		"""
		self.name = name
		self.odds = Fraction(str(odds))
		
	def __eq__(self, other):
		"""
		used to compare equivalence of outcomes on the basis of their names
		
		:param other:(outcome)
		:return: (boolean) equivalence relationship. True for equal False otherwise 
		"""
		return True if self.name == other.name else False
	
	def __ne__(self, other):
		"""
		used to compare equivalence of outcomes on the basis of their names
		
		:param other:(outcome)
		:return: (boolean) equivalence relationship. True for unequal False otherwise 
		"""
		return True if self.name != other.name else False
		
		
	def __hash__(self):
		"""
		perform hashing of the name of the outcome
		used to check equivalence of 2 outcomes on the basis of hash value
		
		:return: (bigint) has value of the name of the object
		"""
		return hash(self.name)
	
	
	def __str__(self):
		"""
		:return: (string) string representation of the object
		"""
		return "{name} ({odds})".format_map(vars(self))


	def __repr__(self):
		"""
		:return: (string) string representation of the object construction
		"""
		return "{class_:s} ({name!r},{odds!r})".format(class_=type(self).__name__,**vars(self))
	
	
	def winAmount(self, amount):
		"""
		Calculates the win amount in case of a favourable outcome
			winningAmount = betamount * odds
			
		:param amount: (numeric) amount bet on the outcome
		:return: (numeric) amount won
		"""
		return self.odds * amount
		