from . import outcome

class CrapsGameState():
    """
    CrapsGameState defines the state-specific behavior of a Craps game. 
    Individual subclasses provide methods used by CrapsTable to validate bets and determine the active bets. 
    Subclasses provide state-specific methods used by a Throw to possibly change the state and resolve bets.    
    """

    def __init__(self, game):
        self.game = game 

    def isValid(self, outcome):
        pass

    def isWorking(self, outcome):
        pass

    def craps(self, throw):
        pass

    def natural(self, throw):
        pass

    def eleven(self, throw):
        pass

    def point(self, throw):
        pass

    def pointOutcome(self):
        pass

    def moveToThrow(self, bet, throw):
        """
        Moves a Come Line or Don’t Come Line bet to a new Outcome based on the current throw. 
        If the value of theThrow is 4, 5, 6, 8, 9 or 10, this delegates the move to the current CrapsGameState object. 
        For values of 4 and 10, the odds are 2:1. For values of 5 and 9, the odds are 3:2. 
        For values of 6 and 8, the odds are 6:5. For other values of theThrow, this method does nothing.
        """
        s = throw.d1 + throw.d2
        if s in (4,5,6,8,9,10):
            if s in (4,10):
                odds = 2
            elif s in (6,8):
                odds = 6/5
            elif s in (5,9):
                odds = 3/2
        bet.outcome = outcome.Outcome('Point', odds) 
    
    def __str__(self):
        pass

class CrapsGamePointOff(CrapsGameState):
    """
    CrapsGamePointOff defines the behavior of the Craps game when the point is off. 
    It defines the allowed bets and the active bets. 
    It provides methods used by a Throw to change the state and resolve bets.
    """

    def __init__(self, game):
        self.pointval = 0
        super().__init__(game)

    def isValid(self, outcome):
        """
        There are two valid Outcomes: Pass Line, Don’t Pass Line. All other Outcomes are invalid.
        """
        if outcome.name in ('Pass Line', 'Dont Pass Line'):
            return True
        else:
            return False

    def isWorking(self, outcome):
        """
        There are six non-working Outcomes: “Come Odds 4”, “Come Odds 5”, “Come Odds 6”, “Come Odds 8”,
        “Come Odds 9” and “Come Odds 10”. All other Outcomes are working
        """
        if 'Come Point Odds' in outcome.name:
            return False
        else:
            return True

    def craps(self, throw):
        """
        When the point is off, a roll of 2, 3 or 12 means the game is an immediate loser. 
        The Pass Line Outcome is a loset. 
        If the Throw value is 12, a Don’t Pass Line Outcome is a push, otherwise the Don’t Pass Line Outcome is a winner. 
        The next state is the same as this state, and the method should return this.
        """
        s = throw.d1 + throw.d2
        for bet in list(self.game.table):
            if bet.outcome.name == 'Pass Line':
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name == 'Dont Pass Line':
                if s == 12:
                    bet.player.stake += bet.amount
                else:
                    bet.player.win(bet)
                self.game.table.bets.remove(bet)
        return self

    def natural(self, throw):
        """
        When the point is off, 7 means the game is an immediate winner. 
        The Pass Line Outcome is a winner, the Don’t Pass Line Outcome is a loser. 
        The next state is the same as this state, and the method should return this.
        """
        for bet in list(self.game.table):
            if bet.outcome.name == 'Pass Line':
                bet.player.win(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name == 'Dont Pass Line':
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
        return self

    def eleven(self, throw):
        """
        When the point is off, 11 means the game is an immediate winner. 
        The Pass Line Outcome is a winner, the Don’t Pass Line Outcome is a loser. 
        The next state is the same as this state, and the method should return this.
        """
        for bet in list(self.game.table):
            if bet.outcome.name == 'Pass Line':
                bet.player.win(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name == 'Dont Pass Line':
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
        return self

    def point(self, throw):
        """
        When the point is off, a new point is established. 
        This method should return a new instance of CrapsGame PointOn created with the given Throw‘s value. 
        Note that any Come Point bets or Don’t Come Point bets that may be on this point are pushed to player: 
        they can’t be legal bets in the next game state.
        """
        s = throw.d1 + throw.d2    
        for bet in list(self.game.table):
            if bet.outcome.name in ('Come Point {s}','Dont Come Point {s}'):
                bet.player.stake += bet.amount
                self.game.table.bets.remove(bet)
        return CrapsGamePointOn(s, self.game)

    def pointOutcome(self):
        """
        Returns the Outcome based on the current point. 
        This is used to create Pass Line Odds or Don’t Pass Odds bets. 
        This delegates the real work to the current CrapsGameState object. 
        Since no point has been established, this returns null.
        """
        return None

    def __str__(self):
        return "This is a come out roll"
    

class CrapsGamePointOn(CrapsGameState):
    """
    CrapsGamePointOn defines the behavior of the Craps game when the point is on. 
    It defines the allowed bets and the active bets. 
    It provides methods used by a Throw to change the state and resolve bets.
    """
    def __init__(self, point, game):
        self.pointval = point
        super().__init__(game)

    def isValid(self, outcome):
        """
        It is invalid to Buy or Lay the Outcomes that match the point. 
        If the point is 6, for example, it is invalid to buy the “Come Point 6” Outcome. 
        All other Outcomes are valid.
        """
        if outcome.name in (f'Buy {self.pointval}', f'Lay {self.pointval}', f'Place Bet {self.pointval}'):
            return False
        else: 
            return True

    def isWorking(self, outcome):
        """
        All Outcomes are working
        """
        return True

    def craps(self, throw):
        """
        When the point is on, 2, 3 and 12 do not change the game state. 
        The Come Line Outcome is a loser, the Don’t
        Come Line Outcome is a winner. 
        The next state is the same as this state, and the method should return this.
        """
        s = throw.d1 + throw.d2
        for bet in list(self.game.table):
            if bet.outcome.name == 'Come Line':
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name == 'Dont Come Line':
                bet.player.win(bet)
                self.game.table.bets.remove(bet)        
        return self

    def natural(self, throw):
        """
        When the point is on, 7 means the game is a loss. 
        Pass Line Outcomes lose, as do the pass-line odds Outcome s based on the point. 
        Don’t Pass Line Outcomes win, as do all Don’t Pass odds Outcome based on the point. 
        The Come Line Outcome is a winner, the Don’t Come Line Outcome is a loser. 
        However, all Come Point number Outcomes and Come Point Number odds Outcome are all losers. 
        All Don’t Come Point number Outcomes and Don’t Come Point odds Outcomes are all winners. 
        The next state is a new instance of the CrapsGamePointOff state.
        """
        s = throw.d1 + throw.d2
        for bet in list(self.game.table):
            if bet.outcome.name in ('Pass Line','Pass Line Odds','Dont Come Line') \
            or 'Come Point' in bet.outcome.name \
            or 'Come Point Odds' in bet.outcome.name \
            or 'Buy' in bet.outcome.name \
            or 'Lay' in bet.outcome.name \
            or 'Place' in bet.outcome.name :
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name in ('Dont Pass Line','Dont Pass Line Odds','Come Line') \
            or 'Dont Come Point' in bet.outcome.name \
            or 'Dont Come Point Odds' in bet.outcome.name:
                bet.player.win(bet)
                self.game.table.bets.remove(bet)
        return CrapsGamePointOff(self.game)

    def eleven(self, throw):
        """
        When the point is on, 11 does not change the game state. 
        The Come Line Outcome is a winner, and the Don’t Come Line Outcome is a loser. 
        The next state is the same as this state, and the method should return this.
        """
        s = throw.d1 + throw.d2
        for bet in list(self.game.table):
            if bet.outcome.name in ('Dont Come Line'):
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name in ('Come Line'):
                bet.player.win(bet)
                self.game.table.bets.remove(bet)
        return self

    def point(self, throw):
        """
        When the point is on and the value of throw doesn’t match point, then the various Come Line bets can be resolved. 
        Come Point Outcome s for this number (and their odds) are winners. 
        Don’t Come Line Outcome s for this number (and their odds) are losers. 
        Other Come Point number and Don’t Come Point numbers remain, unresolved. Any Come Line bets are moved to the Come Point number Outcomes. 

        When the point is on and the value of throw matches point, the game is a winner. 
        Pass Line Outcomes are all winners, as are the behind the line odds Outcomes. 
        Don’t Pass line Outcomes are all losers, as are the Don’t Pass Odds Outcomes. 
        Come Line bets are moved to thee Come Point number Outcomes. 
        Don’t Come Line bets are moved to be Don’t Come number Outcomes. 
        The next state is a new instance of the CrapsGamePointOff state.
        """
        s = throw.d1 + throw.d2
        if s != self.pointval:
            for bet in list(self.game.table):
                if bet.outcome.name in ('Come Point {s}','Come Point Odds {s}', 'Buy {s}', 'Lay {s}', 'Place {s}'):
                    bet.player.win(bet)
                    self.game.table.bets.remove(bet)
                elif bet.outcome.name in ('Dont Come Point {s}','Dont Come Point Odds {s}'):
                    bet.player.lose(bet)
                    self.game.table.bets.remove(bet)
                elif bet.outcome.name == 'Come Line':
                    self.game.moveToThrow(bet, throw)
                elif bet.outcome.name == 'Dont Come Line':
                    self.game.moveToThrow(bet, throw)
            return self
        elif s == self.pointval:
            for bet in list(self.game.table):
                if bet.outcome.name in ('Pass Line', 'Pass Line Odds'):
                    bet.player.win(bet)
                    self.game.table.bets.remove(bet)
                elif bet.outcome.name in ('Dont Pass Line','Dont Pass Line Odds'):
                    bet.player.lose(bet)
                    self.game.table.bets.remove(bet)
                elif bet.outcome.name == 'Come Line':
                    self.game.moveToThrow(bet, throw)
                elif bet.outcome.name == 'Dont Come Line':
                    self.game.moveToThrow(bet, throw)
            return CrapsGamePointOff(self.game)

    def pointOutcome(self):
        return None

    def __str__(self):
        return "This is a point roll"
