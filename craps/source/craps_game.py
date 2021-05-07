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
            print("Pass Line Bets lose, Don't Pass win")
        else:
            """
            Come Line bets are an immediate loss; 
            Don’t Come Line bets are an immediate win. 
            The state doesn’t change.
            """
            print("Come Line Bets lose, Don't Come win")

    def natural(self):
        if self.point == 0:
            """
            this was a come out roll: Pass Line bets are an immediate win; 
            Don’t Pass Line bets are an immediate loss.
            """
            print("Pass Line Bets win, Don't Pass lose")
        else:        
            """
            Come Line bets are an immediate win; 
            Don’t Come bets are an immediate loss; 
            the point is also reset to zero because the game is over.
            Also, hardways bets are all losses.
            """
            self.point = 0
            print("Come Line Bets win, Don't Come lose,") 
            print("State is reset to start of the game")

    def eleven(self):
        if self.point == 0:
            """
            this is a come out roll: Pass Line bets are an immediate win; 
            Don’t Pass Line bets are an immediate loss.
            """
            print("Pass Line Bets win, Don't Pass lose")
        else:
            """
            Come Line bets are an immediate win; 
            Don’t Come bets are an immediate loss. 
            The game state doesn’t change.
            """
            print("Come Line Bets win, Don't Come lose")

    def pointRoll(self, point):
        if self.point == 0:
            self.point = point
            print("Point Roll. State change to on.")
        else:
            if self.point == point:
                """
                Pass Line bets and associated odds bets are winners; 
                Don’t Pass bets and associated odds bets are losers; 
                the point is reset to zero
                """
                print("Pass Line and Odds win, Don't Pass and Odds lose")
                print("State change back to start of the game")
                self.point = 0
            else:
                """
                the state doesn’t change; 
                however, Come point and Don’t come point bets may be resolved. 
                Additionally, hardways bets may be resolved.
                """
                print("No State change, Come Line Bets may resolve")

                
    def __str__(self):
        return "Point Off" if self.point == 0 else "Point On"

    def isAllowed(self, outcome):
        if self.point == 0:
            if outcome in ("Pass", "Don't Pass", "Come", "Don't Come"):
                return True
            else:
                return False
        else:
            return True

    def isWorking(self, outcome):
        if self.point == 0:
            if outcome in ("Come"):
                return False
            else:
                return True
        return False        

        