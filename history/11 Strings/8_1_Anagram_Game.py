import random

def select_random_word():
    # Add more words to the list for variety
    word_list = ["python", "guitar", "programming", "keyboard", "computer", "shampoo"]
    return random.choice(word_list)

def scramble_word(word):
    # Scramble the letters of the word
    scrambled_word = ''.join(random.sample(word, len(word)))
    return scrambled_word

def play_anagrams_game():
    # Select a random word
    original_word = select_random_word()

    # Scramble the word
    scrambled_word = scramble_word(original_word)

    print("Welcome to the Anagrams Game!")
    print("Try to unscramble the following word:")
    print(scrambled_word)

    # Get the player's guess
    player_guess = input("Your guess: ")

    # Check if the guess is correct
    if player_guess.lower() == original_word.lower():
        print("Congratulations! You guessed it correctly.")
    else:
        print(f"Sorry, the correct word was {original_word}.")

# Play the game
play_anagrams_game()