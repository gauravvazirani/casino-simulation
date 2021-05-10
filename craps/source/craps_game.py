import craps_game_state

class CrapsGame():
    """
    Class to perform simulation of a game of craps
    """
    def __init__(self, dice, table):
        self.dice = dice
        self.table = table 
        self.state = craps_game_state.CrapsGamePointOff(self)

    def cycle(self, player):
        player.table = self.table
        while player.playing():
            player.placeBets()
            throw = self.dice.next()
            throw.updateGame(self)
            for bet in self.table:
                if throw.resolveOneRoll(bet) or throw.resolveHardways(bet):
                    self.table.bets.remove(bet)
            player.rounds_to_go -= 1

    def moveToThrow(self, bet, throw):
        self.state.moveToThrow(bet, throw)

    def reset(self):
        self.table.clear()
        self.point = 0
        self.state = craps_game_state.CrapsGamePointOff(self)
