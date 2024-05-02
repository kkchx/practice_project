import random
# Define ranks, suits, and create a deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

random.shuffle(deck)
# Example: Accessing the first card in the deck

card = deck.pop()
print(card)
print("The card is: ",card['rank'], "of", card['suit'])