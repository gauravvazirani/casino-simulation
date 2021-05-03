from random_event import RandomEvent
class Throw(RandomEvent):
    def __init__(self, d1, d2, *outcomes):
        self.d1 = d1
        self.d2 = d2 
        super.__init__(outcomes)

    def hard(self):
        return self.d1 == self.d2

    def updateGame(self, game):
        pass

    def __str__(self):
        return f"{self.d1}, {self.d2}"

class NaturalThrow(Throw):
    def __init__(self, d1, d2, *outcomes):
        super.__init__(d1, d2, *outcomes)
        if d1 + d2 != 7:
            raise Exception("Invalid Declaration for Natural Throw, Dice Sum Mismatch.")
        
    def hard(self):
        return False

    def updateGame(self, game):
        game.natural()

class CrapsThrow(Throw):
    def __init__(self, d1, d2, *outcomes):
        super.__init__(d1, d2, *outcomes)
        if d1 + d2 not in (2, 3, 12):
            raise Exception("Invalid Declaration for Craps Throw, Dice Sum Mismatch.")

    def updateGame(self, game):
        game.craps()

class ElevenThrow(Throw):
    def __init__(self, d1, d2, *outcomes):
        super.__init__(d1, d2, *outcomes)
        if d1 + d2 != 11:
            raise Exception("Invalid Declaration for Eleven Throw, Dice Sum Mismatch.")

    def hard(self):
        return False

    def updateGame(self, game):
        game.eleven()

class PointThrow(Throw):
    def __init__(self, d1, d2, *outcomes):
        super.__init__(d1, d2, *outcomes)
        if d1 + d2 not in (4, 5, 6, 8, 9, 10):
            raise Exception("Invalid Declaration for Point Throw, Dice Sum Mismatch.")

    def updateGame(self, game):
        game.point()
    