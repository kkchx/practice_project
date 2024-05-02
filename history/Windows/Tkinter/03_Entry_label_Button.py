import tkinter as tk
window = tk.Tk()
lbl_caption = tk.Label(text="First name")
ent_firstname = tk.Entry()
btn_confirm = tk.Button(text="Confirm")

lbl_caption.pack()
ent_firstname.pack()
btn_confirm.pack()

window.mainloop()


