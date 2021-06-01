from . import bet
from . import player

class RoulettePlayer(player.Player):
    """
    Implementation of Player interface for the game of roulette.
    """

    def __init__(self, table, wheel):
        super().__init__(wheel)
        self.table = table
        self.wheel = wheel
        self.rounds_to_go = 250
        self.stake = 1000
    
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
        bet_amount = 10
        black = self.wheel.all_outcomes.get('Black')
        self.table.placeBet(bet.Bet(bet_amount ,black), game)
        self.stake -= bet_amount

    def winners(self, winning_outcomes):
        pass