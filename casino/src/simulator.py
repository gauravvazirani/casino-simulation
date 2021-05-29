from .integer_list import IntegerStatistics

from copy import deepcopy
import csv

class Simulator():
    """
    Class which simualtes Sessions of game play.
    It initialises the various components and stores the results after running
    a session of multiple cycles of play.
    """

    def __init__(self, game, player):        
        self.game = game
        self.player = player
        self.durations = IntegerStatistics()
        self.maxima =  IntegerStatistics()
        self.report = []

    def session(self, player):
        """
        One or more cycles. 
        The session begins with a player having their full stake. 
        A session ends when the play elects to leave or can no longer participate. 
        """
        duration = 0
        max_stake = player.stake
        before  = player.stake
        while player.playing():
            self.game.cycle(player)
            player.rounds_to_go -= 1
            max_stake = max(max_stake, player.stake)
            duration += 1 
        return duration, max_stake , before - player.stake 

    def gather(self, sessions):
        """
        Executes the number of game sessions in samples. 
        Every session returns the duration and the maximum stake value in the session.  
        These two metrics are appended to the durations list and the maxima list.
        The durations and maxima lists are printed on stdout. 
        """
        index = 1
        while index <= sessions:
            duration, max_stake, net_difference = self.session(deepcopy(self.player))
            self.durations.append(duration)
            self.maxima.append(max_stake)
            self.report.append((index, duration, net_difference))
            index += 1            

    def save(self, filename):
        """
        Save findings from the simulation in a file
        """
        with open(filename, 'wb') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(('Session No','Duration in Rounds','Net Won'))
            for row in self.report:
                csv_out.writerow(row)
            csv_out.writerow()
            csv_out.writerow(f"Durations: Mean {self.durations.mean()} and Standard Deviation {self.durations.stdev()}")
            csv_out.writerow()
            csv_out.writerow(f"Maxima: Mean {self.maxima.mean()} and Standard Deviation {self.maxima.stdev()}")
