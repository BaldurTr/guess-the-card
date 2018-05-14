from card import Card
from random import shuffle
from random import choice
from random import random

class Deck:

    def __init__(self, number_cards=52):
        self.suits = { 1 : "Hearts", 2 : "Diamonds", 3 : "Spades", 4 : "Clubs" }
        self.cheat_probability = 0.6

        full_deck = [ Card(self.suits[i], Card.card_names_by_rank[j]) for i in range(1,5) for j in range(1,14) ]
        shuffle(full_deck)

        if 1 < number_cards < 52:
            self.deck = full_deck[:number_cards]
        else:
            self.deck = full_deck
    
    def deal_card(self):
        if not self.isEmpty():
            return self.deck.pop()

    def should_cheat(self):
        return random() <= self.cheat_probability

    def deal_favorable_dealer_card(self, card, guess):
        if not self.isEmpty():
            if self.should_cheat():
                comparer = lambda x: x >= card if guess == 'l' else lambda x: x <= card
                favorable_cards = list(filter(comparer, self.deck))
                if favorable_cards: 
                    cheat_card = choice(favorable_cards)
                    self.deck.remove(cheat_card)
                    return cheat_card
            print("Failed tp cheat")
            return self.deck.pop()


    def isEmpty(self):
        return not self.deck