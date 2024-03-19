import random
#Define ranks suits, and create a deck of cards
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Hearts','Diamonds','Clubs','Spades']


def compare_cards(card1, card2):
    # compare two cards and return
    # 1 if the card is higher
    # -1 if the card is lower
    # in all other cases
    rank_order = ranks.index(card1['rank']) - ranks.index(card2['rank'])
    return 1 if rank_order > 0 else -1 if rank_order < 0 else 0


deck = [{'rank': rank, 'suit': suit}for rank in ranks for suit in suits]
random.shuffle(deck)
score = 0

for i in range(1,26,1):
    print("round",i)
    card = deck.pop()
    card2 = deck.pop()
    result = compare_cards(card2, card)
    print("the card is: ", card['rank'], "of", card['suit'])
    print("Choose if the next card is higher or lower? h/l: ")

    try:
        choice = str.lower(input())
    except ValueError:
        print("Please enter h/l(higher or lower)")
    else:
        print("the next card is: ", card2['rank'], "of", card2['suit'])

        if result == 1: #the card is higher
            if choice == "h": #user thinks the card is higher
                score+=20
                print("You win current score is",score)
            elif card == "l":
                score-=20
                print("You lose current score is",score)
        elif result == -1:
            if choice == "l":
                score+=20
                print("You win current score is",score)
            elif choice == "h":
                score-=20
                print("You lose current score is",score)
        else:
            print("It's a tie")