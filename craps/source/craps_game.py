import craps_game_state
class CrapsGame():
    """
    Class to perform simulation of a game of craps
    """
    def __init__(self, dice, table):
        self.dice = dice
        self.table = table 
        self.point = 0
        self.state = craps_game_state.CrapsGamePointOff(self)

    def cycle(self, player):
        pass



    def moveToThrow(self, bet, throw):
        s = throw.d1 + throw.d2
        if s in (4,5,6,8,9,10):
            if s in (4,10):
                odds = 2
            elif s in (6,8):
                odds = 6/5
            elif s in (5,9):
                odds = 3/2
            oc = outcome.Outcome(f'Point {s}', odds) 
        bet.set_outcome(oc)

    def reset(self):
        self.table.clear()
        self.point = 0
        self.state = craps_game_state.CrapsGamePointOff(self)
