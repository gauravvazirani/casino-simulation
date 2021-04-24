import bet

class Passenger57():
    def __init__(self):
        self.balance = 1000

    def placeBets(self, table, wheel):
        """
        used to place a bet of amount 10 on outcome 'Black' 
        on the table
        """
        black = wheel.all_outcomes.get('Black')
        table.placeBet(bet.Bet(10 ,black))
    
    def win(self, bet):
        """
        used to update passenger balance with the winning amount 
        at the end of the game

        :param bet: (Bet)
        """
        self.balance += bet.winAmount()

    def lose(self, bet):
        """
        used to update passenger balance with the losing amount 
        at the end of the game

        :param bet: (Bet)
        """
        self.balance -= bet.loseAmount()
