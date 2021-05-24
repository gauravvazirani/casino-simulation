from . import outcome

class CrapsGameState():
    
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

    def __init__(self, game):
        self.pointval = 0
        super().__init__(game)

    def isValid(self, outcome):
        if outcome.name in ('Pass Line', 'Dont Pass Line'):
            return True
        else:
            return False

    def isWorking(self, outcome):
        if 'Come Point Odds' in outcome.name:
            return False
        else:
            return True

    def craps(self, throw):
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
        for bet in list(self.game.table):
            if bet.outcome.name == 'Pass Line':
                bet.player.win(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name == 'Dont Pass Line':
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
        return self

    def eleven(self, throw):
        for bet in list(self.game.table):
            if bet.outcome.name == 'Pass Line':
                bet.player.win(bet)
                self.game.table.bets.remove(bet)
            elif bet.outcome.name == 'Dont Pass Line':
                bet.player.lose(bet)
                self.game.table.bets.remove(bet)
        return self

    def point(self, throw):
        s = throw.d1 + throw.d2    
        for bet in list(self.game.table):
            if bet.outcome.name in ('Come Point {s}','Dont Come Point {s}'):
                bet.player.stake += bet.amount
                self.game.table.bets.remove(bet)
        return CrapsGamePointOn(s, self.game)

    def pointOutcome(self):
        return None

    def __str__(self):
        return "This is a come out roll"
    

class CrapsGamePointOn(CrapsGameState):

    def __init__(self, point, game):
        self.pointval = point
        super().__init__(game)

    def isValid(self, outcome):
        if outcome.name in (f'Buy {self.pointval}', f'Lay {self.pointval}', f'Place Bet {self.pointval}'):
            return False
        else: 
            return True

    def isWorking(self, outcome):
        return True

    def craps(self, throw):
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
