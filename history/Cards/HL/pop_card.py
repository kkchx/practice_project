import random
# Define ranks, suits, and create a deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

random.shuffle(deck)
# Example: Accessing the first card in the deck

flag = 0
i = 0
while flag == 0:

    card = deck[i]
    i+=1
    print(card)
    print("Would you like to continue?")
    response = str.lower(input())
    if response=='y':
        flag = 0
    else: flag = 1