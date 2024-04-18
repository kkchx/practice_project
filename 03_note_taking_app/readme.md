
# Note-Taking Program Documentation

## Task
The task was to create a console-based note-taking program allowing users to create, read, edit, and delete text notes <br>
you can also exit the program by typing **5** in the input

## Implementation
The program is implemented in Python. It provides a menu-driven interface to manage notes stored as text files. It uses <br>
basic file handling operations and a while loop for continuous interaction.

## Functions
1. create_note() <br>
    Prompts the user to enter a note name and text.<br>
    Validates the note name to contain only alphanumeric characters. <br>
    Builds the note by calling build_note().


2. build_note(note_text, note_name) <br>
    Writes the provided note_text to a text file named after note_name. <br>


3. read_note() <br>
    Prompts the user to enter the name of the note to read. <br>
    Checks if the note file exists and reads its content if found. <br>


4. edit_note() <br>
    Prompts the user to enter the name of the note to edit. <br>
    Displays the current content of the note. <br>
    Allows the user to enter new text for the note, then calls build_note() to update it. <br>


5. delete_note() <br>
    Prompts the user to enter the name of the note to delete. <br>
    Checks if the note file exists and deletes it if found. <br>


6. print_menu() <br>
    Prints the menu options for the user to choose from. <br>


7. main() <br>
    The main function that drives the program. <br>
    Uses a while loop to continuously display the menu and handle user input until the user chooses to quit. <br>
These functions collectively provide the functionality for creating, reading, editing, and deleting notes within the <br>
program.