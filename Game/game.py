
from card import Card
from card_printer import ascii_version_of_card, ascii_version_of_hidden_card
from deck import Deck
from utils import clear_screen


class OverUnder:
    ''' The game Over-Under is a simple guessing game where in a dealer
    and a guesser play for points. A dealer deals out one facedown card
    and a faceup card and the guesser guesses if tha facedown card is over
    or under the faceup one. If he is correct he gets a point otherwise the
    dealer gets a point. A half deck is used for the game.
    '''

    def __init__(self):
        self.dealer_points, self.guesser_points = 0, 0
        self.deck = Deck(26)


    def guesser_won(self, facedown, faceup, guess):
        return (guess == "l" and facedown < faceup) or (guess == "h" and facedown > faceup)

    def get_guess(self):
        guess = input("Is the face down card higher(h) or lower(l)?: ")

        while guess not in ["h", "l"]:
            guess = input("Please select either 'h' for 'higher' or 'l' for 'lower': ")
        
        return guess

    def print_score(self):
        print("Guesser: {0} points, Dealer {1} points".format(self.guesser_points, self.dealer_points))

    def pre_guess_prompt(self, facedown, faceup):
        self.print_score()
        print(ascii_version_of_hidden_card(facedown, faceup))

    def card_reveal(self, facedown, faceup):
        self.print_score()
        print(ascii_version_of_card(facedown, faceup))

    def update_score(self, facedown, faceup, guess):
        if self.guesser_won(facedown, faceup, guess):
                self.guesser_points = self.guesser_points + 1
        else:
            self.dealer_points = self.dealer_points + 1
    
    def print_winner(self):
        self.print_score()
        winner = "Guesser" if self.guesser_points > self.dealer_points else "Dealer"
        points = max(self.guesser_points, self.dealer_points)

        print("Winner is {0} with {1} points. Congratulations!".format(winner, points))

    def play(self):

        while not self.deck.isEmpty():

            facedown = self.deck.deal_card()
            faceup = self.deck.deal_card()

            self.pre_guess_prompt(facedown, faceup)

            guess = self.get_guess()

            self.update_score(facedown, faceup, guess)
            clear_screen()

            self.card_reveal(facedown, faceup)
            
            input("Press any key for next draw...")
            
            clear_screen()

        self.print_winner()

if __name__ == "__main__":
    game = OverUnder()
    game.play()
