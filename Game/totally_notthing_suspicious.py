from random import random

cheat_probability = 0.65

def should_cheat():
        return random() <= cheat_probability