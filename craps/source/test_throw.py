import unittest
import throw
import craps_game 
import outcome

class TestThrow(unittest.TestCase):

    def setUp(self):
        self.throw = throw.Throw(1,2)
        self.game = craps_game.CrapsGame()

    def test_hard(self):
        self.assertEqual(self.throw.hard(), False)
        self.throw.d1 = 2
        self.assertEqual(self.throw.hard(), True)

    def test_updateGame(self):
        self.assertEqual(self.game.point,0)
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.point,0)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestNaturalThrow(unittest.TestCase):

    def setUp(self):
        self.throw = throw.NaturalThrow(3,4)
        self.game = craps_game.CrapsGame()

    def test_hard(self):
        self.assertEqual(self.throw.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.point,0)
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.point,0)

        self.game.point=1
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.point,0)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestCrapsThrow(unittest.TestCase):

    def setUp(self):
        self.throw_hard = throw.CrapsThrow(1,1)
        self.throw_easy = throw.CrapsThrow(2,1)
        self.game = craps_game.CrapsGame()

    def test_hard(self):
        self.assertEqual(self.throw_hard.hard(), True)
        self.assertEqual(self.throw_easy.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.point,0)
        self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.point,0)

        self.game.point=1
        self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.point,1)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestElevenThrow(unittest.TestCase):

    def setUp(self):
        self.throw = throw.ElevenThrow(6,5)
        self.game = craps_game.CrapsGame()

    def test_hard(self):
        self.assertEqual(self.throw.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.point,0)
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.point,0)

        self.game.point=1
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.point,1)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestPointThrow(unittest.TestCase):

    def setUp(self):
        self.throw_hard = throw.PointThrow(3,3)
        self.throw_easy = throw.PointThrow(3,2)
        self.game = craps_game.CrapsGame()

    def test_hard(self):
        self.assertEqual(self.throw_hard.hard(), True)
        self.assertEqual(self.throw_easy.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.point,0)
        self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.point,6)

        self.throw_easy.updateGame(self.game)
        self.assertEqual(self.game.point,6)    

        self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.point,0)

    def tearDown(self):
        self.throw = None
        self.game = None

if __name__ == '__main__':
    unittest.main()
