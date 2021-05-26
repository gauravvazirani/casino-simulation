class RandomEventFactory():
    """
    Base class for random event factories such as dice for craps and wheel for roulette.
    """

    def __init__(self, rng):
        self.rng = rng
        self.initialize()

    def initialize(self):
        """
        Initializes the random event factory with appropriate outcome of random events.
        """
        pass

    def next(self):
        """
        returns the next set of outcomes choosen as a result of a random event.
        """
        pass
