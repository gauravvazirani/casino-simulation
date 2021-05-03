import random

class Dice():
    def __init__(self):
        self.all_throws = {}
        self.rng = random.Random()

    def addThrow(self, throw):
        self.all_throws.update({throw.get_key():throw})

    def next(self):
        keys = [keys for keys in self.all_throws]
        return self.all_throws.get(self.rng.choice(keys))

    def getThrow(self, d1, d2):
        key = 6 * (d1 - 1) + (d2 - 1)
        return self.all_throws.get(key)    
