from card import Card
from random import shuffle
from random import choice
from random import random
from totally_nothing_suspicious import should_cheat

class Deck:
    """Holds a single deck of cards and contains several
    methods to use on the deck such as deal_card and the
    slightly better deal_favorable_dealer_card which comes
    in handy every so often.
    """

    def __init__(self):
        self.suits = { 1 : "Hearts", 2 : "Diamonds", 3 : "Spades", 4 : "Clubs" }
        full_deck = [ Card(self.suits[i], Card.card_names_by_rank[j]) for i in range(1,5) for j in range(1,14) ]
        shuffle(full_deck)
        self.number_of_cards = 26

        self.deck = full_deck
    
    def deal_card(self, card:Card=None):
        if self.isEmpty(): 
            return

        if card:
            returnCard = card
            self.deck.remove(card)
        else:    
            returnCard = self.deck.pop()

        self.lower_card_count()
        return returnCard

    def lower_card_count(self):
        self.number_of_cards = self.number_of_cards - 1

    def deal_favorable_dealer_card(self, card, guess):
        if not self.isEmpty():
            if should_cheat(card.points):
                #print("I chose to cheat!")
                comparer = lambda x: x >= card if guess == 'l' else lambda x: x <= card
                favorable_cards = list(filter(comparer, self.deck))
                if favorable_cards:
                    cheat_card = choice(favorable_cards)
                    return self.deal_card(cheat_card)
                #print("I failed to cheat!")
            #print("I chose not to cheat!")
            return self.deal_card()

    def choose_from_cheat_card_list(self, selectedCard, cards):
        cardsDict = { c.points: [] for c in cards }
        for k, v in cards:
            cardsDict[k].Append(v)
        return cardsDict
        
    def isEmpty(self):
        return self.number_of_cards == 0