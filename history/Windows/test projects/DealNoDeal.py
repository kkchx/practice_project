import tkinter as tk
import random

class DealOrNoDeal:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-fullscreen', True)
        self.cases = list(range(1, 27))
        self.values = [0.01, 1, 10, 100, 500, 1000, 5000, 10000, 50000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000, 2000000, 3000000, 4000000, 5000000, 7500000, 10000000, 20000000, 25000000, 50000000]

        self.player_case = None
        self.banker_offer = None

        self.create_ui()

    def create_ui(self):
        self.instructions_label = tk.Label(self.root, text="Welcome to Deal or No Deal! Pick your case.")
        self.instructions_label.pack()

        self.case_buttons_frame = tk.Frame(self.root)
        self.case_buttons_frame.pack()

        for case in self.cases:
            button = tk.Button(self.case_buttons_frame, text=str(case), command=lambda c=case: self.choose_case(c))
            button.pack(side=tk.LEFT)

        self.instruction_label = tk.Label(self.root, text="Choose your lucky case.")
        self.instruction_label.pack()

        self.deal_button = tk.Button(self.root, text="Deal", command=self.deal, state="disabled")
        self.deal_button.pack()

        self.no_deal_button = tk.Button(self.root, text="No Deal", command=self.no_deal, state="disabled")
        self.no_deal_button.pack()

    def choose_case(self, case):
        if self.player_case is None:
            self.player_case = case
            self.instruction_label.config(text=f"You chose case {case}. Now, choose 6 cases to open.")
            self.case_buttons_frame.children[str(case)].config(state="disabled")
        else:
            self.instruction_label.config(text="You've already chosen a case.")

    def deal(self):
        if self.player_case is not None:
            self.banker_offer = self.calculate_banker_offer()
            result = "DEAL! The bank's offer is ${:,.2f}.".format(self.banker_offer)
            self.instruction_label.config(text=result)
            self.deal_button.config(state="disabled")
            self.no_deal_button.config(state="disabled")

    def no_deal(self):
        if self.player_case is not None:
            if len(self.cases) == 1:
                result = "NO DEAL! You rejected the bank's offer and won ${:,.2f}!".format(self.values[self.cases[0] - 1])
                self.instruction_label.config(text=result)
            else:
                case_to_open = random.choice(self.cases)
                self.cases.remove(case_to_open)
                value = self.values[case_to_open - 1]
                result = f"No deal! You opened case {case_to_open} with ${value:,.2f}."
                self.instruction_label.config(text=result)
                self.case_buttons_frame.children[str(case_to_open)].config(state="disabled")

    def calculate_banker_offer(self):
        remaining_value = sum(self.values[i - 1] for i in self.cases) / len(self.cases)
        return remaining_value * 0.5  # A simple offer calculation

if __name__ == "__main__":
    root = tk.Tk()
    game = DealOrNoDeal(root)
    root.mainloop()
