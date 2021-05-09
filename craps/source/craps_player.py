import outcome 

class CrapsPlayer():

    def __init__(self, table):
        self.pass_line = outcome.Outcome('Pass Line', 1)
        self.working_bet = None
        self.table = table  
