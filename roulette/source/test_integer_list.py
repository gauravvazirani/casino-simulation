import unittest
from integer_list import IntegerStatistics 

class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.test_list = IntegerStatistics([10,8,13,9,11,14,6,4,12,7,5])

    def test_mean(self):
        self.assertEqual(self.test_list.mean(), 9.0)

    def test_stddev(self):
        m = self.test_list.mean()
        self.assertEqual(sum(self.test_list), 99)
        self.assertEqual(len(self.test_list), 11)
        self.assertEqual(m, 9.0)
        self.assertEqual(sum((x-m)**2 for x in self.test_list), 110.0)
        self.assertEqual(round(self.test_list.stdev(),3), 3.317)
    
    def tearDown(self):
        self.test_list = None

if __name__ == '__main__':
    unittest.main()