import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Colorful Tic-Tac-Toe - Player vs Player")
        self.root.configure(bg="#F9F7F7")
        self.root.resizable(False, False)

        self.current_player = "X"
        self.board = [""] * 9
        self.buttons = []

        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="🎉 Tic-Tac-Toe Game 🎉", font=("Helvetica", 20, "bold"), bg="#F9F7F7", fg="#3F72AF")
        title.grid(row=0, column=0, columnspan=3, pady=10)

        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 30, "bold"), width=5, height=2,
                            bg="#DBE2EF", fg="#112D4E", activebackground="#F9F7F7",
                            command=lambda i=i: self.button_click(i))
            btn.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        self.status_label = tk.Label(self.root, text="Player X's Turn", font=("Helvetica", 14), bg="#F9F7F7", fg="#112D4E")
        self.status_label.grid(row=4, column=0, columnspan=3, pady=10)

        reset_btn = tk.Button(self.root, text="🔄 Reset Game", font=("Helvetica", 12), bg="#3F72AF", fg="white",
                              activebackground="#112D4E", command=self.reset_game)
        reset_btn.grid(row=5, column=0, columnspan=3, pady=10)

    def button_click(self, index):
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player,
                                       fg="#FF2E63" if self.current_player == "X" else "#08D9D6")
            if self.check_winner(self.current_player):
                self.status_label.config(text=f"🎉 Player {self.current_player} Wins!")
                self.disable_buttons()
            elif "" not in self.board:
                self.status_label.config(text="It's a Draw! 🤝")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.status_label.config(text=f"Player {self.current_player}'s Turn")

    def check_winner(self, player):
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combos:
            if all(self.board[i] == player for i in combo):
                for i in combo:
                    self.buttons[i].config(bg="#FFB400")  # highlight winning combo
                return True
        return False

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for btn in self.buttons:
            btn.config(text="", state="normal", bg="#DBE2EF")
        self.status_label.config(text="Player X's Turn")


# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
