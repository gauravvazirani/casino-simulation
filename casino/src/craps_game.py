from . import craps_game_state
from . import game

class CrapsGame(game.Game):
    """
    Class to perform simulation of a game of craps
    """
    def __init__(self, dice, table):
        super().__init__(dice, table)
        self.state = craps_game_state.CrapsGamePointOff(self)

    def cycle(self, player):
        player.table = self.table
        round=1
        while player.playing():
            print(f'\nRound {round}')
            print(f'Stake:{player.stake}\nRounds Left:{player.rounds_to_go}')
            print(f'State of the Game:{self.state}')
            player.placeBets(self.state.pointval)
            print(f'Bets Placed on Table:{self.table.bets}')
            throw = self.eventFactory.next()
            print(f'Throw Value - d1:{throw.d1} d2:{throw.d2}')
            self.state = throw.updateGame(self)
            for bet in self.table:
                if throw.resolveOneRoll(bet) or throw.resolveHardways(bet):
                    self.table.bets.remove(bet)
            print(f'Bets on Table post Resolution:{self.table.bets}')
            print(f'Stake:{player.stake}')
            round+=1
            if player.rounds_to_go > 0:
                player.rounds_to_go -= 1

    def isValid(self, outcome):
        return self.state.isValid(outcome)

    def moveToThrow(self, bet, throw):
        self.state.moveToThrow(bet, throw)

    def reset(self):
        super().reset()
        self.state = craps_game_state.CrapsGamePointOff(self)
