class CrapsGame():
    """
    Class to perform simulation of a game of craps
    """
    def __init__(self):
        self.point = 0

    def craps(self):
        if self.point == 0:
            """
            this was a come out roll: Pass Line bets are an immediate loss, 
            Don’t Pass Line bets are an immediate win.
            """
        else:
            """
            Come Line bets are an immediate loss; 
            Don’t Come Line bets are an immediate win. 
            The state doesn’t change.
            """

    def natural(self):
        if self.point == 0:
            """
            this was a come out roll: Pass Line bets are an immediate win; 
            Don’t Pass Line bets are an immediate loss.
            """
        else:        
            """
            Come Line bets are an immediate win; 
            Don’t Come bets are an immediate loss; 
            the point is also reset to zero because the game is over.
            Also, hardways bets are all losses.
            """

    def eleven(self):
        if self.point == 0:
            """
            this is a come out roll: Pass Line bets are an immediate win; 
            Don’t Pass Line bets are an immediate loss.
            """
        else:
            """
            Come Line bets are an immediate win; 
            Don’t Come bets are an immediate loss. 
            The game state doesn’t change.
            """

    def point(self, point):
        if self.point == 0:
            self.point = point
        else:
            if self.point == point:
                """
                Pass Line bets and associated odds bets are winners; 
                Don’t Pass bets and associated odds bets are losers; 
                the point is reset to zero
                """
                self.point = 0
            else:
                """
                the state doesn’t change; 
                however, Come point and Don’t come point bets may be resolved. 
                Additionally, hardways bets may be resolved.
                """
                
    def __str__(self):
        return "Point Off" if self.point == 0 else "Point On"
        