from card import Card
from random import shuffle

class Deck:

    def __init__(self, number_cards=52):
        self.suits = { 1 : "Hearts", 2 : "Diamonds", 3 : "Spades", 4 : "Clubs" }

        full_deck = [ Card(self.suits[i], Card.card_names_by_rank[j]) for i in range(1,5) for j in range(1,14) ]
        shuffle(full_deck)

        if 1 < number_cards < 52:
            self.deck = full_deck[:number_cards]
        else:
            self.deck = full_deck
    
    def deal_card(self):
        if not self.isEmpty():
            return self.deck.pop()

    def isEmpty(self):
        return not self.deck