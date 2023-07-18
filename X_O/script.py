import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkFont

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Define font
        self.my_font = tkFont.Font(family="Helvetica", size=32, weight="bold")

        # Style
        self.window.configure(bg='lightblue')
        self.window.geometry('600x600')

        self.player_turn = "X"

        self.board = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(tk.Button(self.window, text=" ", width=2, height=1, 
                                     command=lambda i=i, j=j: self.click(i, j), font=self.my_font, 
                                     bg='white', activebackground='white'))
                row[-1].grid(row=i, column=j, padx=5, pady=5, ipadx=20, ipady=20)
            self.board.append(row)

    def click(self, i, j):
        if self.board[i][j]['text'] == " ":
            self.board[i][j]['text'] = self.player_turn

            if self.check_win(self.player_turn):
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.window.quit()

            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self, player):
        for i in range(3):
            if all(self.board[i][j]['text'] == player for j in range(3)):
                return True
            if all(self.board[j][i]['text'] == player for j in range(3)):
                return True

        if self.board[0][0]['text'] == self.board[1][1]['text'] == self.board[2][2]['text'] == player:
            return True

        if self.board[0][2]['text'] == self.board[1][1]['text'] == self.board[2][0]['text'] == player:
            return True

        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
