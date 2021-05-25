import unittest
from src import throw
from src import craps_game 
from src import outcome
from src import dice
from src import table
from src import craps_game_state

class TestThrow(unittest.TestCase):

    def setUp(self):
        self.throw = throw.Throw(1,2)
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  craps_game.CrapsGame(self.dice, self.table)
        self.table.setGame(self.game)        
 
    def test_hard(self):
        self.assertEqual(self.throw.hard(), False)
        self.throw.d1 = 2
        self.assertEqual(self.throw.hard(), True)

    def test_updateGame(self):
        self.assertEqual(self.game.state.pointval,0)
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,0)
    
    def test_add1Roll(self):
        self.assertEqual(len(self.throw.win_1roll),0)
        self.assertEqual(len(self.throw.lose_1roll),0)
        self.throw.add1Roll(
            winners=[outcome.Outcome('Pass',1)],
            losers=[outcome.Outcome('Dont Pass',1)]
            )
        self.assertEqual(len(self.throw.win_1roll),1)
        self.assertEqual(len(self.throw.lose_1roll),1)

    def test_addHardways(self):
        self.assertEqual(len(self.throw.win_hardway),0)
        self.assertEqual(len(self.throw.lose_hardway),0)
        self.throw.addHardways(
            winners=[outcome.Outcome('Hardway 4',1)],
            losers=[outcome.Outcome('Easyway 4',1)]
            )
        self.assertEqual(len(self.throw.win_hardway),1)
        self.assertEqual(len(self.throw.lose_hardway),1)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestNaturalThrow(unittest.TestCase):

    def setUp(self):
        self.throw = throw.NaturalThrow(3,4)
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  craps_game.CrapsGame(self.dice, self.table)
        self.table.setGame(self.game)        

    def test_hard(self):
        self.assertEqual(self.throw.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.state.pointval,0)
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,0)

        self.game.state = craps_game_state.CrapsGamePointOn(4, self.game)
        self.game.state = self.throw.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,0)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestCrapsThrow(unittest.TestCase):

    def setUp(self):
        self.throw_hard = throw.CrapsThrow(1,1)
        self.throw_easy = throw.CrapsThrow(2,1)
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  craps_game.CrapsGame(self.dice, self.table)
        self.table.setGame(self.game)        

    def test_hard(self):
        self.assertEqual(self.throw_hard.hard(), True)
        self.assertEqual(self.throw_easy.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.state.pointval,0)
        self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,0)

        self.game.state.pointval=1
        self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,1)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestElevenThrow(unittest.TestCase):

    def setUp(self):
        self.throw = throw.ElevenThrow(6,5)
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  craps_game.CrapsGame(self.dice, self.table)
        self.table.setGame(self.game)        

    def test_hard(self):
        self.assertEqual(self.throw.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.state.pointval,0)
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,0)

        self.game.state.pointval=1
        self.throw.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,1)

    def tearDown(self):
        self.throw = None
        self.game = None

class TestPointThrow(unittest.TestCase):

    def setUp(self):
        self.throw_hard = throw.PointThrow(3,3)
        self.throw_easy = throw.PointThrow(3,2)
        self.dice = dice.Dice()
        self.table = table.Table(minimum=1, maximum=1000)
        self.game =  craps_game.CrapsGame(self.dice, self.table)
        self.table.setGame(self.game)        

    def test_hard(self):
        self.assertEqual(self.throw_hard.hard(), True)
        self.assertEqual(self.throw_easy.hard(), False)

    def test_updateGame(self):
        self.assertEqual(self.game.state.pointval,0)
        self.game.state = self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,6)

        self.game.state = self.throw_easy.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,6)    

        self.game.state = self.throw_hard.updateGame(self.game)
        self.assertEqual(self.game.state.pointval,0)

    def tearDown(self):
        self.throw = None
        self.game = None

if __name__ == '__main__':
    unittest.main()
