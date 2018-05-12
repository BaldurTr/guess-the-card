from game import OverUnder
from human import Human
from robot import Robot
from utils import get_percentage



game = OverUnder(Human())
game.play()
# winner_list = []
# total_rounds = 10000
# for _ in range(total_rounds):
#     winner_list.append(game.play())
#     game.reset()

# dealer_wins = winner_list.count("Dealer")
# print("Dealer won {0} games from {1} with a {2:.2f}% win percentage!".format(dealer_wins, total_rounds, get_percentage(total_rounds, dealer_wins)))