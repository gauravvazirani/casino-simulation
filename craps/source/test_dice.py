import unittest
import dice
import outcome
import throw
import random

class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = dice.Dice()
        self.outcome1 = outcome.Outcome('Any Craps',3)
        self.outcome2 = outcome.Outcome('Hard 4',30)
        self.outcome3 = outcome.Outcome('Easy 6',10)
        self.throw1 = throw.Throw(1,2,[self.outcome1])
        self.throw2 = throw.Throw(2,2,[self.outcome2])
        self.throw3 = throw.Throw(2,4,[self.outcome3])
        self.dice.rng.seed(1)        

    def test_addThrow(self):
        self.assertEqual(len(self.dice.all_throws),0)
        self.dice.addThrow(self.throw1)
        self.assertEqual(len(self.dice.all_throws),1)
        self.dice.addThrow(self.throw2)
        self.dice.addThrow(self.throw3)
        self.assertEqual(len(self.dice.all_throws),3)

    def test_next(self):
        self.dice.addThrow(self.throw1)
        self.dice.addThrow(self.throw2)
        self.dice.addThrow(self.throw3)
        test_rng = random.Random()
        test_rng.seed(1)
        keys = [keys for keys in self.dice.all_throws]
        self.assertEqual(
            self.dice.next(),
            self.dice.all_throws.get(test_rng.choice(keys))
            )
        self.assertEqual(
            self.dice.next(),
            self.dice.all_throws.get(test_rng.choice(keys))
            )
        self.assertEqual(
            self.dice.next(),
            self.dice.all_throws.get(test_rng.choice(keys))
            )

    def test_getThrow(self):
        self.dice.addThrow(self.throw1)
        self.dice.addThrow(self.throw2)
        self.dice.addThrow(self.throw3)
        self.assertEqual(self.dice.getThrow(1,2),self.throw1)
        self.assertEqual(self.dice.getThrow(2,2),self.throw2)
        self.assertEqual(self.dice.getThrow(2,4),self.throw3)

    def tearDown(self):
        self.dice = None
        self.outcome1 = None
        self.outcome2 = None
        self.outcome3 = None
        self.throw1 = None
        self.throw2 = None
        self.throw3 = None
         
if __name__ == '__main__':
    unittest.main()
