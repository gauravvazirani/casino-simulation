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
        
        :param player: (Player) 
        """
        print("player_stake",player.stake)
        print("player_rounds",player.rounds_to_go)
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
            duration, max_stake, net_difference = self.session(self.player)
            self.durations.append(duration)
            self.maxima.append(max_stake)
            self.report.append((index, duration, net_difference, max_stake))
            index += 1            
            self.player.table.clear()
            self.player.__init__(self.player.table, self.player.wheel)


    def save(self, filename):
        """
        Save findings from the simulation in a file
        """
        with open(filename, 'w') as out:
            csv_out = csv.writer(out)
            csv_out.writerow((f'Simulated results for {type(self.game).__name__} using {type(self.player).__name__} strategy',))
            csv_out.writerow('')
            csv_out.writerow(('Session No','Duration in Rounds','Net Won','Maximum Stake'))
            for row in self.report:
                csv_out.writerow(row)
            csv_out.writerow('')
            csv_out.writerow((f'Durations: Mean {round(self.durations.mean(),2)} and Standard Deviation {round(self.durations.stdev(),2)}',))
            csv_out.writerow('')
            csv_out.writerow((f'Maxima: Mean {round(float(self.maxima.mean()),2)} and Standard Deviation {round(self.maxima.stdev(),1)}',))
