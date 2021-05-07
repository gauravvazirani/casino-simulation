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
	
	
	def winAmount(self, amount, random_event=None):
		"""
		Calculates the win amount in case of a favourable outcome
			winningAmount = betamount * odds
			
		:param amount: (numeric) amount bet on the outcome
		:return: (numeric) amount won
		"""
		if random_event is not None:
			return random_event.odds * amount
		else:
			return self.odds * amount

class OutcomeField(Outcome):
	"""
	Class to handle special case where the odds of the outcome
	depends on the sum of the throw.
	In case of field outcome, if sum of the dice is 2 or 12 then the 
	odds are 2:1 otherwise its 1:1
	"""

	def winAmount(self, amount, throw):
		"""
		Calculates the winning amount according to the odds associated
		with the sum of dice numbers fo the throw event passed as input.

		:param amount: (numeric) Amount bet on the field outcome
		:param throw: (Throw)
		"""
		if throw.d1+throw.d2 in (2, 12):
			throw.odds = Fraction(2,1)			
		else:
			throw.odds = Fraction(1,1)
		return super().winAmount(amount, throw)

	def __str__(self):
		return f"Field (1:1, 2 and 12 - 2:1)"


class OutcomeHorn(Outcome):
	"""
	Class to handle special case where the odds of the outcome
	depends on the sum of the throw.
	In case of horn outcome, if sum of the dice is 2 or 12 then the 
	odds are 27:4 otherwise its 3:1
	"""

	def winAmount(self, amount, throw):
		"""
		Calculates the winning amount according to the odds associated
		with the sum of dice numbers fo the throw event passed as input.

		:param amount: (numeric) Amount bet on the horn outcome
		:param throw: (Throw)
		"""
		if throw.d1+throw.d2 in (2, 12):
			throw.odds = Fraction(27, 4)			
		else:
			throw.odds = Fraction(3, 1)
		return super().winAmount(amount, throw)

	def __str__(self):
		return f"Horn (2 and 12 - 27:4, 3 and 11 - 3:1)"
