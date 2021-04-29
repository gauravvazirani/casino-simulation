from integer_list import IntegerStatistics

class Simulator():

    def __init__(self, game, player, stake=100, init_duration=250, samples=50):
        self.game = game
        self.player = player
        self.init_stake =  stake
        self.player.setStake(self.player.bet_amount * self.init_stake)
        self.init_duration = init_duration
        self.player.setRounds(self.init_duration)
        self.samples = samples
        self.durations = IntegerStatistics()
        self.maxima =  IntegerStatistics()

    def session(self, debug=False):
        """
        One or more cycles. 
        The session begins with a player having their full stake. 
        A session ends when the play elects to leave or can no longer participate. 
        """
        max_stake = self.player.stake
        while self.player.playing():
            if debug:
                print(f"Starting Round {self.init_duration - self.player.rounds_to_go + 1}")
                print(f"Player Balance: {self.player.stake} points")
                print(f"Bet Amount: {self.player.bet_amount} points")
            self.game.cycle(self.player)
            self.player.rounds_to_go -= 1
            max_stake = max(max_stake, self.player.stake) 
        return self.init_duration - self.player.rounds_to_go, max_stake 

    def gather(self):
        """
        Executes the number of game sessions in samples. 
        Every session returns the duration and the maximum stake value in the session.  
        These two metrics are appended to the durations list and the maxima list.
        The durations and maxima lists are printed on stdout. 
        """
        index = 1
        print(f"Running Simulation for {self.samples} Sessions")
        print("Index Duration MaxStake")
        while index <= self.samples:
            self.player.setStake(self.player.bet_amount * self.init_stake)
            self.player.setRounds(self.init_duration)
            duration, max_stake = self.session()
            print(index,' '*4, duration,' '*4, max_stake)
            self.durations.append(duration)
            self.maxima.append(max_stake)
            index += 1
        print(f"Maxima: Mean {self.maxima.mean()} and Standard Deviation {self.maxima.stdev()}")
        print(f"Durations: Mean {self.durations.mean()} and Standard Deviation {self.durations.stdev()}")


