from random_event import RandomEvent
class Throw(RandomEvent):
    """
    Throw is a collection of outcomes.
    It resembles outcomes from 1 throw of a dice.
    """
    def __init__(self, d1, d2, winners=[], losers=[]):
        self.d1 = d1
        self.d2 = d2
        self.winners = set(winners)
        self.losers = set(losers)
        self.win_1roll = set()
        self.lose_1roll = set()
        self.win_hardway = set()
        self.lose_hardway = set()  

    def add1Roll(self, winners, losers):
        """
        Adds outcomes to the one-roll winners and one-roll losers Sets.

        :param winners: (set) All the outcomes which will be paid as winners for this Throw.
        :param losers: (set) All the outcomes which will be considered as losers for this Throw.
        """
        self.win_1roll.update(winners)
        self.lose_1roll.update(losers)

    def addHardways(self, winners, losers):
        """
        Adds outcomes to the hardway winners and hardway losers Sets.

        :param winners: (set) All the outcomes which will be paid as winners for this Throw.
        :param losers: (set) All the outcomes which will be considered as losers for this Throw.
        """
        self.win_hardway.update(winners)
        self.lose_hardway.update(losers)

    def hard(self):
        """
        :returns: (boolean) whether or not throw was a hard throw
        """
        return self.d1 == self.d2

    def updateGame(self, game):
        """
        method responsible for resolving multiple roll propositions and
        causing appropriate state change of the game.
        """
        pass

    def resolveOneRoll(self, bet):
        """
        pay the player if the bet is in the one roll winners set.
        return true to indicate the bet must be removed from the table 
        if the bet is present in either one roll outcomes.

        :param bet: The bet to to be resolved

        :returns: (boolean) 
        """
        if bet.outcome in self.win_1roll:
            bet.player.win(bet)
            return True
        elif bet.outcome in self.lose_1roll:
            return True
        else:
            return False

    def resolveHardways(self, bet):
        """
        pay the player if the bet is in the hardway winners set.
        return true to indicate the bet must be removed from the table 
        if the bet is present in either hardway outcomes.

        :param bet: The bet to to be resolved

        :returns: (boolean) 
        """
        if bet.outcome in self.win_hardway:
            bet.player.win(bet)
            return True
        elif bet.outcome in self.lose_hardway:
            return True
        else:
            return False

    def __str__(self):
        """
        string representation of the object
        """
        return f"{self.d1}, {self.d2}"

    def getKey(self):
        return (self.d1,self.d2)

class NaturalThrow(Throw):
    """
    Case when sum of two dice is 7
    """
    def __init__(self, d1, d2, *outcomes):
        super().__init__(d1, d2, *outcomes)
        if d1 + d2 != 7:
            raise Exception("Invalid Declaration for Natural Throw, Dice Sum Mismatch.")
        
    def hard(self):
        return False

    def updateGame(self, game):
        return game.state.natural(self)

class CrapsThrow(Throw):
    """
    Case when sum of dice is one out of 2, 3 and 12.
    """
    def __init__(self, d1, d2, *outcomes):
        super().__init__(d1, d2, *outcomes)
        if d1 + d2 not in (2, 3, 12):
            raise Exception("Invalid Declaration for Craps Throw, Dice Sum Mismatch.")

    def updateGame(self, game):
        return game.state.craps(self)

class ElevenThrow(Throw):
    """
    Case when sum of dice is 11
    """
    def __init__(self, d1, d2, *outcomes):
        super().__init__(d1, d2, *outcomes)
        if d1 + d2 != 11:
            raise Exception("Invalid Declaration for Eleven Throw, Dice Sum Mismatch.")

    def hard(self):
        return False

    def updateGame(self, game):
        return game.state.eleven(self)

class PointThrow(Throw):
    """
    Case when sum of dice is one out of 4, 5, 6, 8, 9, 10. 
    """
    def __init__(self, d1, d2, *outcomes):
        super().__init__(d1, d2, *outcomes)
        if d1 + d2 not in (4, 5, 6, 8, 9, 10):
            raise Exception("Invalid Declaration for Point Throw, Dice Sum Mismatch.")
        self.point=d1+d2

    def updateGame(self, game):
        return game.state.point(self)
    