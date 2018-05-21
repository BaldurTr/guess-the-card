import unittest
from deck import Deck
from card import Card
from game import OverUnder
from human import Human

class DeckTest(unittest.TestCase):
    def testGenerateDeck(self):
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)

class GameTest(unittest.TestCase):
    def testGuesserWinsWithLowerCard(self):
        game = OverUnder(Human())

        facedownCard = Card("Spade", "3")
        faceupCard = Card("Diamond", "5")
        guess = "l"
        self.assertTrue(game.guesser_won(facedownCard, faceupCard, guess))

    def testGuesserWinsWithHigherCard(self):
        game = OverUnder(Human())

        facedownCard = Card("Spade", "8")
        faceupCard = Card("Diamond", "5")
        guess = "h"
        self.assertTrue(game.guesser_won(facedownCard, faceupCard, guess))

    def testDealerWinsWithEqualCard(self):
        game = OverUnder(Human())

        facedownCard = Card("Spade", "3")
        faceupCard = Card("Diamond", "3")
        guess = "l"
        self.assertFalse(game.guesser_won(facedownCard, faceupCard, guess))

if __name__ == "__main__":
    unittest.main()