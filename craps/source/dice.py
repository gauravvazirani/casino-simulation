import random

class Dice():
    """
    Two Dice are rolled on every cycle of the game.
    Dice stop at a random set of numbers between 1 and 6,
    Thus its a collectioin of throws.
    """
    def __init__(self):
        self.all_throws = {}
        self.rng = random.Random()

    def addThrow(self, throw):
        """
        Adds the given Throw to the mapping maintained by this instance of Dice. 
        The key for this Throw is available from the Throw.getKey() method.
        
        :param throw: (Throw) 
        """
        self.all_throws.update({throw.getKey():throw})

    def next(self):
        """
        First, get the list of keys from the throws.
        The random.Random.choice() method will select one of the available keys 
        from the the list. 
        This is used to get the corresponding Throw from the throws Map.

        :return: (Throw) randomly selected Throw.
        """
        keys = [keys for keys in self.all_throws]
        return self.all_throws.get(self.rng.choice(keys))

    def getThrow(self, d1, d2):
        """
        This method takes a particular combination of dice, 
        locates (or creates) a NumberPair, and returns the 
        appropriate Throw.
        
        :param d1: (int) Number on the 1st die
        :param d2: (int) Number on the 2nd die

        :return: (Throw) Throw correspoding to the input dice numbers
        """
        key = (d1,d2)
        return self.all_throws.get(key)    
