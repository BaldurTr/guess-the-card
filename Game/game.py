
from card import Card
from card_printer import ascii_version_of_card, ascii_version_of_hidden_card
from deck import Deck
from utils import clear_screen
from dealer import Dealer
from human import Human

GAME_DECK_SIZE = 26

class OverUnder:
    ''' The game Over-Under is a simple guessing game where in a dealer
    and a guesser play for points. A dealer deals out one facedown card
    and a faceup card and the guesser guesses if tha facedown card is over
    or under the faceup one. If he is correct he gets a point otherwise the
    dealer gets a point. A half deck is used for the game.
    '''

    def __init__(self, player=None):
        self.dealer = Dealer()
        self.player = player
        self.deck = Deck()
        self.game_counter = 0
        self.remaining_cards = GAME_DECK_SIZE

    def guesser_won(self, facedown, faceup, guess):
        return (guess == "l" and facedown < faceup) or (guess == "h" and facedown > faceup)

    def print_score(self):
        print("Guesser: {0} points, Dealer {1} points".format(self.player.points, self.dealer.points))

    def pre_guess_prompt(self, faceup):
        if not self.player.isRobot:
            self.print_score()
            print(ascii_version_of_hidden_card(faceup))

    def card_reveal(self, facedown, faceup):
        if not self.player.isRobot:
            self.print_score()
            print(ascii_version_of_card(facedown, faceup))
            input("Press enter for next draw...")
            clear_screen()

    def update_score(self, facedown, faceup, guess):
        if self.guesser_won(facedown, faceup, guess):
                self.player.add_point()
        else:
            self.dealer.add_point()
        if not self.player.isRobot:
            clear_screen()
    
    def find_winner(self):
        self.game_counter = self.game_counter + 1
        return self.dealer if self.player < self.dealer else self.player

    def print_winner(self, winner):
        if not winner.isRobot:
            self.print_score()
            print("Winner is {0} with {1} points. Congratulations!".format(winner.name, winner.points))
            input("Press enter to exit")

    def reset(self):
        self.deck = Deck()
        self.dealer.points = 0
        self.player.points = 0
        self.remaining_cards = GAME_DECK_SIZE

    def discard_used_cards(self):
        self.remaining_cards = self.remaining_cards - 2

    def play(self):
        while self.remaining_cards > 0:
            faceup = self.deck.deal_card()
            self.pre_guess_prompt(faceup)
            guess = self.player.get_guess(faceup)
            facedown = self.deck.deal_favorable_dealer_card(faceup, guess)
            self.update_score(facedown, faceup, guess)
            self.card_reveal(facedown, faceup)
            self.discard_used_cards()

        winner = self.find_winner()
        self.print_winner(winner)

        return winner.name

if __name__ == "__main__":
    game = OverUnder(Human())
    game.play()
