import random

# Define ranks, suits, and create a deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Function to compare two cards and return 1 if card1 is higher, -1 if card2 is higher, and 0 if they are equal
def compare_cards(card1, card2):
    rank_order = ranks.index(card1['rank']) - ranks.index(card2['rank'])
    return 1 if rank_order > 0 else -1 if rank_order < 0 else 0

score = 0

# Main game loop
while True:
    # Draw two cards
    current_card = deck.pop()
    next_card = deck.pop()

    print(f'Current card: {current_card["rank"]} of {current_card["suit"]}')

    # Ask the player to guess
    guess = input('Will the next card be higher (h) or lower (l)? Enter "h" or "l": ')

    # Compare the cards
    result = compare_cards(next_card, current_card)

    # Check if the player's guess is correct
    if (guess == 'h' and result == 1) or (guess == 'l' and result == -1):
        print(f'Next card: {next_card["rank"]} of {next_card["suit"]}')
        print('Correct!')
        score += 1
    elif result == 0:
        print(f'Next card: {next_card["rank"]} of {next_card["suit"]}')
        print('It\'s a tie!')
    else:
        print(f'Next card: {next_card["rank"]} of {next_card["suit"]}')
        print('Incorrect. Game over.')
        break

print(f'Your final score is: {score}')