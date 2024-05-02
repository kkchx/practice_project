'''pip install pyjokes'''
import pyjokes

def generate_joke():
    joke = pyjokes.get_joke()
    return joke

print("Welcome to the Joke Generator!")

while True:
    input_user = input("Press Enter to get a joke... Press 0 to exit.")
    if input_user=='0':
        break
    else:
        joke = generate_joke()
        print("\nHere's your joke:")
        print(joke)


