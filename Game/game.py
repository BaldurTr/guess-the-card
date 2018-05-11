from card import Card
from card_printer import (
    ascii_version_of_card, 
    ascii_version_of_hidden_card
    )

# TEST CASES
test_card_1 = Card('Diamonds', '4')
test_card_2 = Card('Clubs', 'Ace')
test_card_3 = Card('Spades', 'Jack')
test_card_4 = Card('Hearts', '10')

print(ascii_version_of_card(test_card_1, test_card_2, test_card_3, test_card_4))
print(ascii_version_of_hidden_card(test_card_1, test_card_2, test_card_3, test_card_4))
# print(ascii_version_of_hidden_card(test_card_1, test_card_2))

