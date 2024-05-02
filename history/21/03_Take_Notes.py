import os

def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w") as file:
        file.write(note_text)

def create_note():
    note_name = input("Enter note name: ")
    note_text = input("Enter note text: ")
    build_note(note_text, note_name)

def read_note():
    note_name = input("Enter note name: ")
    if os.path.isfile(f"{note_name}.txt"):
        with open(f"{note_name}.txt", "r") as file:
            content = file.read()
            print(content)
    else:
        print("Note not found.")

def edit_note():
    note_name = input("Enter note name: ")
    if os.path.isfile(f"{note_name}.txt"):
        with open(f"{note_name}.txt", "r") as file:
            content = file.read()
            print(f"Current content:\n{content}")
            new_text = input("Enter new note text: ")
        build_note(new_text, note_name)
    else:
        print("Note not found.")

def delete_note():
    note_name = input("Enter note name: ")
    if os.path.isfile(f"{note_name}.txt"):
        os.remove(f"{note_name}.txt")
        print(f"Note '{note_name}' deleted.")
    else:
        print("Note not found.")

def main():
    while True:
        print("\nOptions:")
        print("1. Create a new note")
        print("2. Read a note")
        print("3. Edit a note")
        print("4. Delete a note")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            create_note()
        elif choice == "2":
            read_note()
        elif choice == "3":
            edit_note()
        elif choice == "4":
            delete_note()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()