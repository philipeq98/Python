import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]

        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            if self.check_win(self.current_player):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_board()
            elif self.check_tie():
                messagebox.showinfo("Tie", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
        else:
            messagebox.showerror("Invalid Move", "That position is already taken. Try again.")

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)) or \
                    all(self.board[j][i] == player for j in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or \
                all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def check_tie(self):
        return all(cell != " " for row in self.board for cell in row)

    def reset_board(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToeGUI()
    game.run()
