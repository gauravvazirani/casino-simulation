import unittest
from src import outcome
from src import craps_sevencountplayer
from src import table
from src import nochange_betting
from src import martingale_betting
from src import bet1326_betting
from src import bet
from src import dice
from src import craps_game
from src import craps_game_state

class TestSevenCountPlayer(unittest.TestCase):
    def setUp(self):
        self.line_outcome = outcome.Outcome('Pass Line', 1) 
        self.odds_outcome = outcome.Outcome('Pass Line Odds', 1)
        self.seven_outcome = outcome.Outcome('Number 7', 4)
        self.strategy_nochange = nochange_betting.NoChangeBetting(
            self.line_outcome
        )
        self.strategy_bet1326 = bet1326_betting.Craps1326Betting(
            self.odds_outcome
        )
        self.strategy_martingale = martingale_betting.MartingaleBetting(
            self.seven_outcome
        )
        self.table = table.Table(5,1000)
        self.game = craps_game.CrapsGame(
            table=self.table,
            dice=dice.Dice()
        ) 
        self.table.setGame(self.game)
        self.player = craps_sevencountplayer.CrapsSevenCountPlayer(
           table = self.table,
           line_strategy = self.strategy_nochange,
           odds_strategy = self.strategy_bet1326,
           seven_strategy = self.strategy_martingale
        )

    def test_placeBets(self):
        self.player.placeBets(0)
        self.game.state = craps_game_state.CrapsGamePointOn(
            game=self.game, point=5)
        self.player.placeBets(5)
        self.assertEqual(len(self.game.table.bets), 2)
        for multiplier in  [1,3,2,6]:
            self.player.placeBets(5)
            test_bet = self.player.odds_strategy.createBet(
                self.player)
            self.assertEqual(test_bet.amount, 
                multiplier * self.player.odds_strategy.bet_amount) 
            self.player.win(
                bet.Bet(10, self.odds_outcome)
            )
        self.assertEqual(len(self.game.table.bets), 2)
        for _ in range(3):
                self.player.placeBets(5)
        self.assertEqual(len(self.game.table.bets), 3)
        self.assertEqual(
            self.game.table.bets[2].outcome, self.seven_outcome)
            
    def test_win(self):
        self.player.win(
            bet.Bet(10, self.line_outcome)
        )
        test_bet = self.player.line_strategy.createBet(
            self.player)
        self.assertEqual(test_bet.amount, 10)

        self.player.win(
            bet.Bet(10, self.odds_outcome)
        )    
        test_bet = self.player.odds_strategy.createBet(
            self.player)
        self.assertEqual(test_bet.amount, 
            3 * self.player.odds_strategy.bet_amount) 

        self.player.win(
            bet.Bet(10, self.seven_outcome)
        )        
        test_bet = self.player.seven_strategy.createBet(
            self.player)
        self.assertEqual(test_bet.amount, 10)

    def test_lose(self):
        self.player.lose(
            bet.Bet(10, self.line_outcome)
        )
        test_bet = self.player.line_strategy.createBet(
            self.player)
        self.assertEqual(test_bet.amount, 10)

        self.player.lose(
            bet.Bet(10, self.odds_outcome)
        )    
        test_bet = self.player.odds_strategy.createBet(
            self.player)
        self.assertEqual(test_bet.amount, 
            self.player.odds_strategy.bet_amount) 

        self.player.lose(
            bet.Bet(10, self.seven_outcome)
        )        
        test_bet = self.player.seven_strategy.createBet(
            self.player)
        self.assertEqual(
            test_bet.amount, 
            2 * self.player.odds_strategy.bet_amount)
            
    def tearDown(self):
        self.line_outcome = None
        self.odds_outcome = None
        self.strategy_nochange = None
        self.strategy_martingale = None
        self.table = None
        self.game = None
        self.player = None

if __name__ == '__main__':
    unittest.main()




