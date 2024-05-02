import tkinter as tk

# Function to update the number of panes in the PanedWindow
def update_panes():
    num_panes = int(pane_spinbox.get())
    for child in paned_window.panes():
        paned_window.forget(child)  # Remove existing panes
    for i in range(num_panes):
        new_pane = tk.Frame(paned_window, background=colors[i % len(colors)])
        label = tk.Label(new_pane, text=f"Pane {i + 1}", padx=10, pady=10)
        button = tk.Button(new_pane, text=f"Button {i + 1}")
        label.pack()
        button.pack()
        paned_window.add(new_pane)

# Create the main window
root = tk.Tk()
root.title("Spinbox and PanedWindow Demo")

# Define some colors for the panes
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# Create a Label and Spinbox to set the number of panes
pane_label = tk.Label(root, text="Number of Panes:")
pane_label.pack()
pane_spinbox = tk.Spinbox(root, from_=1, to=6)
pane_spinbox.pack()
update_button = tk.Button(root, text="Update Panes", command=update_panes)
update_button.pack()

# Create a PanedWindow with an initial pane
paned_window = tk.PanedWindow(root, orient=tk.VERTICAL)
update_panes()  # Initialize with one pane

# Pack the PanedWindow
paned_window.pack(fill=tk.BOTH, expand=True)

# Start the tkinter event loop to keep the program running
root.mainloop()
