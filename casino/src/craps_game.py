from . import craps_game_state
from . import game

class CrapsGame(game.Game):
    """
    Implementation of the general game interface for the game of craps.    
    """
    def __init__(self, dice, table):
        super().__init__(dice, table)
        self.state = craps_game_state.CrapsGamePointOff(self)

    def cycle(self, player):
        """
        simulates a single round of single player craps
        1 player places its bets
        2 game fetches the winning outcomes from a 
        single thriow of the dice
        3 game updates its own state based on the throw and updates player balances 
        based on the outcome being a winning or losing outcome.
        4 game resolves the hardway and one way propositions if any.

        :param player: (Passenger57)
        """    
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
        """
        :return: (Boolean) whether or not the outcome is valid for a given game state.
        """
        return self.state.isValid(outcome)

    def moveToThrow(self, bet, throw):
        """
        change the outcome of a line bet to a corresponding outcome from a throw object 
        when the state of the game changes from come out roll to point roll.

        :param bet: (Bet) bet to be changed.
        :param throw: (Throw) throw event used to assign new outcomes.  
        """
        self.state.moveToThrow(bet, throw)

    def reset(self):
        """
        chaneges the state back to the initial come out state.
        """
        super().reset()
        self.state = craps_game_state.CrapsGamePointOff(self)
