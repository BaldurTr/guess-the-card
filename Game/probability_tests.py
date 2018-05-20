import unittest
from game import OverUnder
from robot import Robot

class ProbabilityTest(unittest.TestCase):
    def testDealerWinsRobotBetween51and60percentage(self):
        game = OverUnder(Robot())
        total_tries = 10000
        winner_list = []

        for _ in range(total_tries):
            winner_list.append(game.play())
            game.reset()
        
        dealer_wins = winner_list.count("Dealer")

        dealer_win_percentage = (dealer_wins/total_tries)
        self.assertTrue(dealer_win_percentage > 0.51)
        self.assertTrue(dealer_win_percentage < 0.60)

if __name__ == "__main__":
    unittest.main()