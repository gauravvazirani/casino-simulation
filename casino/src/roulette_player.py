from . import bet
from . import player
from .config import PLAYER_STAKE, PLAYER_ROUNDS, RANDOM_BET_AMOUNT as BET_AMOUNT

class RoulettePlayer(player.Player):
    """
    Implementation of Player interface for the game of roulette.
    """

    def __init__(self, table, wheel):
        super().__init__(wheel)
        self.table = table
        self.wheel = wheel
        self.rounds_to_go = PLAYER_ROUNDS
        self.stake = PLAYER_STAKE
        self.bet_amount = BET_AMOUNT
            
    def setRounds(self, rounds_to_go):
        """
        setter method for rounds_to_go

        :param rounds_to_go: (integer) number of rounds the player will play.
        """
        self.rounds_to_go = rounds_to_go

    def setStake(self, stake):
        """
        setter method for stake

        :param stake: (numeric) Net amount that player has in its wallet.
        """
        self.stake = stake

    def playing(self):
        """
        :return: (Boolean) whether or not player is ready to play the next round.
        """
        return True if self.rounds_to_go > 0 and self.stake >= self.table.minimum \
              else False

    def placeBets(self, game):
        """
        Places a bet on the table.
        Deducts the bet amount from player's stake.
        """
        black = self.wheel.all_outcomes.get('Black')
        self.table.placeBet(bet.Bet(self.bet_amount ,black), game)
        self.stake -= self.bet_amount

    def winners(self, winning_outcomes):
        pass