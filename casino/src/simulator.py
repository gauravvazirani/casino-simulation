from .integer_list import IntegerStatistics
from .invalid_bet_exception import InvalidBetException

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
        print("before", before)
        while player.playing():
            try:
                self.game.cycle(player)
            except InvalidBetException as e:
                break
            player.rounds_to_go -= 1
            max_stake = max(max_stake, player.stake)
            duration += 1
        print("after", player.stake) 
        return duration, max_stake , player.stake - before

    def gather(self, sessions, event_factory):
        """
        Executes the number of game sessions in samples. 
        Every session returns the duration and the maximum stake value in the session.  
        These two metrics are appended to the durations list and the maxima list.
        The durations and maxima lists are printed on stdout. 
        """
        index = 1
        init_stake = self.player.stake
        init_rounds = self.player.rounds_to_go
        while index <= sessions:
            duration, max_stake, net_difference = self.session(self.player)
            self.durations.append(duration)
            self.maxima.append(max_stake)
            self.report.append((index, duration, net_difference, max_stake))
            index += 1            
            self.player.table.clear()            
            self.player.__init__(self.player.table, event_factory)
            self.player.setStake(init_stake)
            self.player.setRounds(init_rounds)

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
