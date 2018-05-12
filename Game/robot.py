from player import Player
import random

class Robot(Player):

    def __init__(self):
        super().__init__()

    def get_guess(self):
        return random.choice(self.answers)