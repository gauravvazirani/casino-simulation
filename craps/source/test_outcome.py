import unittest
import outcome

class TestOutcome(unittest.TestCase):

	def test__eq__(self):
		self.assertEqual(outcome.Outcome('red',18)==outcome.Outcome('red',18),True)
		self.assertEqual(outcome.Outcome('red',18)==outcome.Outcome('red',17),True)
		self.assertEqual(outcome.Outcome('red',18)==outcome.Outcome('blue',17),False)
		self.assertEqual(outcome.Outcome('red',18)==outcome.Outcome('blue',18),False)
	
	def test__ne__(self):
		self.assertEqual(outcome.Outcome('red',18)!=outcome.Outcome('red',18),False)
		self.assertEqual(outcome.Outcome('red',18)!=outcome.Outcome('red',17),False)
		self.assertEqual(outcome.Outcome('red',18)!=outcome.Outcome('blue',17),True)
		self.assertEqual(outcome.Outcome('red',18)!=outcome.Outcome('blue',18),True)
		
	def test__hash__(self):
		self.assertEqual(hash(outcome.Outcome('red',18))==hash(outcome.Outcome('red',18)),True)
		self.assertEqual(hash(outcome.Outcome('red',18))==hash(outcome.Outcome('red',17)),True)
		self.assertEqual(hash(outcome.Outcome('red',18))==hash(outcome.Outcome('blue',17)),False)
		self.assertEqual(hash(outcome.Outcome('red',18))==hash(outcome.Outcome('blue',18)),False)
		
	def test__str__(self):
		print("testing str function")
		print(outcome.Outcome('red',18).__str__())
		print(outcome.Outcome('black',18).__str__())
		print(outcome.Outcome('black',20).__str__())
		
	def test__repr__(self):
		print("testing repr function")
		print(outcome.Outcome('red',18).__repr__())		
		print(outcome.Outcome('black',18).__str__())
		print(outcome.Outcome('black',20).__str__())

	def test_winAmount(self):
		self.assertEqual(outcome.Outcome('black',20).winAmount(10),200)
		self.assertEqual(outcome.Outcome('black',10).winAmount(15),150)
	
if __name__=='__main__':
	unittest.main()
			