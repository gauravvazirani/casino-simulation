from .roulette_martingale import RouletteMartingale

class RouletteSevenReds(RouletteMartingale):
    """
    SevenReds is a Martingale player who places bets in Roulette. 
    This player waits until the wheel has spun red 
    seven times in a row before betting black.
    """
    def __init__(self, table, wheel):
        RouletteMartingale.__init__(self, table, wheel)
        self.red_count=7

    def winners(self, winning_outcomes):
        """
        This is notification from the Game of all the winning outcomes. 
        If this vector includes red, redCount is decremented. 
        Otherwise, redCount is reset to 7

        :param winning_outcomes: (Outcome)
        """
        winning_outcome_names = [outcome.name for outcome in winning_outcomes]
        if 'Red' in winning_outcome_names:
            if self.red_count > 0:
                self.red_count -= 1
        else:
            self.red_count = 7

    def placeBets(self):
        """
        If redCount is zero, this places a bet on black, 
        using the bet multiplier.
        """
        if self.red_count == 0:
            RouletteMartingale.placeBets(self)
