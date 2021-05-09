import outcome

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
        # s = throw.d1 + throw.d2
        # if s in (4,5,6,8,9,10):
        #     if s in (4,10):
        #         odds = 2
        #     elif s in (6,8):
        #         odds = 6/5
        #     elif s in (5,9):
        #         odds = 3/2
        #     oc = outcome.Outcome('Point', odds) 
        pass
    
    def __str__(self):
        pass



class CrapsGamePointOff():

    def __init__(self, game):
        super().__init__(game)

    def isValid(self, outcome):
        if outcome.name in ('Pass Line', 'Dont Pass Line'):
            return True
        else 
            return False

    def isWorking(self, outcome):
        if 'Come Odds' in outcome.name:
            return False
        else:
            return True

    def craps(self, throw):
        s = throw.d1 + throw.d2
        for bet in self.game.table:
            if bet.outcome.name == 'Pass':
                bet.player.lose()
                self.game.table.bets.remove(bet)
            elif bet.outcome.name == 'Dont Pass':
                if s == 12:
                    bet.player.stake += bet.amount
                else:
                    bet.player.win(bet)
                self.game.table.bets.remove(bet)
        return self

    def natural(self, throw):
        return self

    def eleven(self, throw):
        return self

    def point(self, throw):
        #push come point and dont come point bets
        return crapsGamePointOn(throw.d1 + throw.d2, self.game)

    def pointOutcome(self):
        return None

    def __str__(self):
        return "This is the come out roll"
    

class CrapsGamePointOn():

    def __init__(self, point, game):
        game.point = point
        super().__init__(game)

    def isValid(self, outcome):
        if outcome.name in (f'Point {self.game.point}'):
            return False
        else 
            return True

    def isWorking(self, outcome):
        return True

    def craps(self, throw):
        return self

    def natural(self, throw):
        return CrapsGamePointOff(self.game)

    def eleven(self, throw):
        return self

    def point(self, throw):
        s = throw.d1 + throw.d2
        if s != self.game.point:
            return self
        else:
            return CrapsGamePointOff(self.game)
        
    def pointOutcome(self):
        return None

    def __str__(self):
        return "This is the come out roll"
