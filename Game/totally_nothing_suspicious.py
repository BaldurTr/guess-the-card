from random import random

MAX_CHEATING_ODDS = 0.90

def should_cheat(points):
        if points in [1,2,12,13]:
            return random() <= MAX_CHEATING_ODDS / 2
        elif points in [3,4,10,11]:
            return random() <= MAX_CHEATING_ODDS / 1.5
        return random() <= MAX_CHEATING_ODDS