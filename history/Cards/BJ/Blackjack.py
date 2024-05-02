import random

# Create a deck of cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']

deck = [{'rank': rank, 'suit': suit} for suit in suits for rank in ranks]

# Define card values
card_values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
               'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

# Initialize player and dealer hands
player_hand = []
dealer_hand = []

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = sum(card_values[card['rank']] for card in hand)
    # Check for aces and adjust the value if necessary
    for card in hand:
        if card['rank'] == 'Ace' and value > 21:
            value -= 10
    return value

# Function to deal a card to a hand
def deal_card(hand):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)

# Initial deal
deal_card(player_hand)
deal_card(dealer_hand)
deal_card(player_hand)
deal_card(dealer_hand)

# Game loop
while True:
    # Display the player's hand and the dealer's upcard
    print(f"Your hand: {', '.join(card['rank'] + ' of ' + card['suit'] for card in player_hand)}")
    print(f"Dealer's upcard: {dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")

    # Check for player blackjack or bust
    if calculate_hand_value(player_hand) == 21:
        print("Blackjack! You win!")
        break
    elif calculate_hand_value(player_hand) > 21:
        print("Bust! You lose.")
        break

    # Ask the player to hit or stand
    choice = input("Do you want to hit or stand? ").strip().lower()

    # Deal a card if the player chooses to hit
    if choice == 'hit':
        deal_card(player_hand)
    elif choice == 'stand':
        # Dealer's turn
        while calculate_hand_value(dealer_hand) < 17:
            deal_card(dealer_hand)

        # Display dealer's hand
        print(f"Dealer's hand: {', '.join(card['rank'] + ' of ' + card['suit'] for card in dealer_hand)}")

        # Determine the winner
        if calculate_hand_value(dealer_hand) > 21:
            print("Dealer busts! You win!")
        elif calculate_hand_value(dealer_hand) > calculate_hand_value(player_hand):
            print("Dealer wins!")
        elif calculate_hand_value(dealer_hand) < calculate_hand_value(player_hand):
            print("You win!")
        else:
            print("It's a tie!")

        break
    else:
        print("Invalid choice. Please enter 'hit' or 'stand'.")