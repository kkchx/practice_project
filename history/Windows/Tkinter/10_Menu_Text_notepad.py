import tkinter as tk
from tkinter import filedialog

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            text = text_widget.get("1.0", "end-1c") #from beginning to the end
            file.write(text)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text only please", "*.txt")])
    if file_path:
        with open(file_path, "r") as file: #with guarantees that file will be properly closed
            text = file.read()
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", text)

def make_bold():
    current_tags = text_widget.tag_names("sel.first")
    if "bold" in current_tags:
        text_widget.tag_remove("bold", "sel.first", "sel.last")
    else:
        text_widget.tag_configure("bold", font=("Courier New", 10, "bold"))
        text_widget.tag_add("bold", "sel.first","sel.last")

# Create the main window
root = tk.Tk()
root.title("Simple Notepad")

# Create a Text widget
text_widget = tk.Text(root, wrap="word")
text_widget.pack(expand="yes", fill="both")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add "Save" and "Open" options in the "File" menu
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Bold", command=make_bold)
edit_menu.add_command(label="Copy", command=make_bold)
edit_menu.add_command(label="Paste", command=make_bold)
root.mainloop()
