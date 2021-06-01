from . import betting_strategy
from . import outcome
from . import bet
from .config import MARTINGALE_BETTING_AMOUNT as BET_AMOUNT

class MartingaleBetting(betting_strategy.BettingStrategy):
    """
    Betting strategy which doubles the betting amount after each loss to 
    recover the amount lost.
    """

    def __init__(self, outcome):
        super().__init__(outcome, BET_AMOUNT) 
        self.loss_count = 0

    def createBet(self, player):
        """
        multiplies current amount with the multiplier which is equal to 2 ** number of losses.
        
        :return: (Bet) bet as a result of updated bet amount.  
        """
        bet_multiple = 2 ** self.loss_count
        return bet.Bet(
            self.bet_amount * bet_multiple, self.outcome, player)

    def win(self):
        """
        resets the loss count back to 0 after each win
        """
        self.loss_count = 0

    def lose(self):
        """
        increments the loss count by 1  after each loss
        """
        self.loss_count += 1
