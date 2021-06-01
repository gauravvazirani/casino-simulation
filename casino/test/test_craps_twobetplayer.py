import unittest
from src import outcome
from src import craps_twobetplayer
from src import table
from src import nochange_betting
from src import martingale_betting
from src import bet
from src import dice
from src import craps_game
from src import craps_game_state

class TestTwoBetPlayer(unittest.TestCase):
    def setUp(self):
        self.line_outcome = outcome.Outcome('Pass Line', 1) 
        self.odds_outcome = outcome.Outcome('Pass Line Odds', 1)
        self.strategy_nochange = nochange_betting.NoChangeBetting(
            self.line_outcome
        )
        self.strategy_martingale = martingale_betting.MartingaleBetting(
            self.odds_outcome
        )
        self.table = table.Table(5,1000)
        self.game = craps_game.CrapsGame(
            table=self.table,
            dice=dice.Dice()
        ) 
        self.table.setGame(self.game)
        self.player = craps_twobetplayer.CrapsTwoBetPlayer(
           self.table,
           dice.Dice()

        )
        self.player.line_strategy = self.strategy_nochange
        self.player.odds_strategy = self.strategy_martingale


    def test_placeBets(self):
        self.assertEqual(len(self.table.bets),0)
        self.player.placeBets(0)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(
            self.table.bets[0].amount, 
            self.strategy_nochange.bet_amount
        )
        self.assertEqual(
            self.table.bets[0].outcome.name, 
            'Pass Line'
        )
        self.player.placeBets(0)
        self.assertEqual(len(self.table.bets), 1)
        self.game.state = craps_game_state.CrapsGamePointOn(
            game=self.game,point=5)
        self.player.placeBets(5)
        self.assertEqual(len(self.table.bets), 2)
        self.assertEqual(
            self.table.bets[1].amount, 
            self.strategy_martingale.bet_amount
        )
        self.assertEqual(
            self.table.bets[1].outcome.name, 
            'Pass Line Odds'
        )
        self.player.placeBets(0)
        self.assertEqual(len(self.table.bets), 2)
        self.player.placeBets(5)
        self.assertEqual(len(self.table.bets), 2)

    def test_win(self):
        self.player.win(
            bet.Bet(amount=10,outcome=self.line_outcome)
        )
        test_bet = self.player.line_strategy.createBet(self.player)
        self.assertEqual(
            test_bet.amount, 
            self.strategy_nochange.bet_amount
        )

        self.player.win(
            bet.Bet(amount=10,outcome=self.odds_outcome)
        )
        self.assertEqual(
            self.player.odds_strategy.loss_count,
            0
        )
        test_bet = self.player.odds_strategy.createBet(self.player)
        self.assertEqual(
            test_bet.amount, 
            self.strategy_martingale.bet_amount
        )

    def test_lose(self):
        self.player.lose(
            bet.Bet(10,self.odds_outcome)
            )
        self.assertEqual(
            self.player.odds_strategy.loss_count,
            1
        )
        test_bet_odds = self.player.odds_strategy.createBet(self.player)
        self.assertEqual(
            test_bet_odds.amount,
            self.strategy_martingale.bet_amount * 2
        )
        self.player.win(
            bet.Bet(amount=10,outcome=self.line_outcome)
        )       
        test_bet_line = self.player.line_strategy.createBet(self.player)
        self.assertEqual(
            test_bet_line.amount,
            self.strategy_nochange.bet_amount
        )
        self.player.win(
            bet.Bet(amount=10,outcome=self.odds_outcome)
        )
        self.assertEqual(
            self.player.odds_strategy.loss_count,
            0
        )
        test_bet_odds = self.player.odds_strategy.createBet(self.player)
        self.assertEqual(
            test_bet_odds.amount,
            self.strategy_martingale.bet_amount
        )
        self.player.win(
            bet.Bet(amount=10,outcome=self.line_outcome)
        )       
        test_bet_line = self.player.line_strategy.createBet(self.player)
        self.assertEqual(
            test_bet_line.amount,
            self.strategy_nochange.bet_amount
        )

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
