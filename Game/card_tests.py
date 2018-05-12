import unittest

from Card import Card


class TestCardComparisons(unittest.TestCase):

    def smaller_card_should_compare_correctly(self):
        smaller = Card('Clubs', '4')
        larger = Card('Hearts', '10')
        self.assertTrue(smaller < larger)

if __name__ == '__main__':
    unittest.main()
