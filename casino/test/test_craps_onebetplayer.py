import unittest
from src import outcome
from src import craps_onebetplayer
from src import table 
from src import nochange_betting
from src import martingale_betting
from src import bet
from src import dice
from src import craps_game

class TestOneBetPlayer(unittest.TestCase):
    def setUp(self):
        self.outcome = outcome.Outcome('Pass Line', 1) 
        self.strategy_nochange = nochange_betting.NoChangeBetting(
            self.outcome
        )
        self.strategy_martingale = martingale_betting.MartingaleBetting(
            self.outcome
        )
        self.table = table.Table(5,1000)
        self.game = craps_game.CrapsGame(
            table=self.table,
            dice=dice.Dice()
        ) 
        self.table.setGame(self.game)
        # self.player = craps_onebetplayer.OneBetPlayer(
        #   table = self.table,
        #   strategy = self.strategy_nochange  
        # )
        self.player = craps_onebetplayer.OneBetPlayer(
           table = self.table,
           dice = dice.Dice()
        )
        self.player.line_strategy = self.strategy_martingale

    def test_placeBets(self):
        self.assertEqual(len(self.table.bets),0)
        self.player.placeBets(0, self.game)
        self.assertEqual(len(self.table.bets), 1)
        self.assertEqual(
            self.table.bets[0].amount, 
            self.strategy_martingale.bet_amount
        )
        self.assertEqual(
            self.table.bets[0].outcome.name, 
            'Pass Line'
        )
        self.player.placeBets(0, self.game)
        self.assertEqual(len(self.table.bets), 1)
        self.player.placeBets(5, self.game)
        self.assertEqual(len(self.table.bets), 1)

    def test_win(self):
        self.player.win(
            bet.Bet(amount=10,outcome=self.outcome)
        )
        self.assertEqual(
            self.player.line_strategy.loss_count,
            0
        )
        test_bet = self.player.line_strategy.createBet(self.player)
        self.assertEqual(
            test_bet.amount, 
            self.strategy_nochange.bet_amount
        )

    def test_lose(self):
        self.player.lose(            
            bet.Bet(amount=10,outcome=self.outcome)
        )
        self.assertEqual(
            self.player.line_strategy.loss_count,
            1
        )
        test_bet = self.player.line_strategy.createBet(self.player)
        self.assertEqual(
            test_bet.amount,
            # self.strategy_martingale.bet_amount
            self.strategy_martingale.bet_amount * 2
        )

        self.player.win(
            bet.Bet(amount=10,outcome=self.outcome)
        )
        self.assertEqual(
            self.player.line_strategy.loss_count,
            0
        )
        test_bet = self.player.line_strategy.createBet(self.player)
        self.assertEqual(
            test_bet.amount,
            self.strategy_martingale.bet_amount
        )

    def tearDown(self):
        self.outcome = None
        self.strategy_nochange = None
        self.strategy_martingale = None
        self.table = None
        self.game = None
        self.player = None

if __name__ == '__main__':
    unittest.main()
