import os
def create_note():
    note_name = input("Enter note name: ")
    if note_name.isalnum():
        note_text = input("Enter note text: ")
        build_note(note_text, note_name)
    else:
        print("Only characters and number allowed, try again")
        return create_note()


def build_note(note_text, note_name):
    with open(f"{note_name}.txt", "w") as file:
        file.write(note_text)


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
            print(f"Current content: {content}")
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


def print_menu():
    print("""Options:
    1. Create a new note
    2. Read a note
    3. Edit a note
    4. Delete a note
    5. Quit""")


def main():
    while True:
        print_menu()
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
main()