import random
# Define ranks, suits, and create a deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

def compare_cards(card1, card2):
    rank_order = ranks.index(card1['rank']) - ranks.index(card2['rank'])
    return 1 if rank_order > 0 else -1 if rank_order < 0 else 0

deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]

random.shuffle(deck)
# Example: Accessing the first card in the deck
score = 0
for i in range(1,8,1):
    print("Round ",i)
    card = deck.pop()
    nextcard = deck.pop()
    print("The card is: ",card['rank'], "of", card['suit'])
    print("Choose if next card higher or lower? h/l")
    choice=str.lower(input())
    print("Next card is: ", nextcard['rank'], "of", nextcard['suit'])
    result=compare_cards(nextcard,card)
    if result==1:
        if choice=='h':
            print('YOU WIN')
            score=score+20
            print("Current score is ", score)
        elif choice=='l':
            print("YOU LOSE")
            score = score - 20
            print("Current score is ", score)
    else:
        if result == -1:
            if choice == 'l':
                print('YOU WIN')
                score = score + 20
                print("Current score is ", score)
            elif choice=='h':
                print("YOU LOSE")
                score = score-20
                print("Current score is ", score)
        else:
            print("It's a tie")
            print("Current score is ", score)


print("Game over! Your score is ",score)