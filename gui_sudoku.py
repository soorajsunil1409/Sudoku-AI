import tkinter as tk
from tkinter import ttk
from threading import Thread
import time

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]

width=70

class Board(tk.Tk):
    slots = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    selected = False

    def __init__(self, board):
        self.board = board

        super().__init__()
        self.title("Sudoku")
        self.geometry(f"{width*9}x{width*9}")
        self.resizable(False, False)

        self.setup_btns()
        self.bind("<Button-2>", self.solve)

        self.mainloop()

    def solve(self, e):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):

            if self.is_valid(i, (row, col)):
                self.after(100)
                self.slots[row][col].configure(text=i, background="red")
                self.update()

                if self.solve(None):
                    return True

                self.slots[row][col].configure(text="")
                self.update()

        return False

        
    def setup_btns(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] != 0:
                    lbl = tk.Label(self, text=self.board[i][j], borderwidth=2, relief=tk.GROOVE, font=("Helvetica", 30))
                    lbl.place(x=j*width, y=i*width, height=width, width=width)
                    self.slots[i][j] = lbl
                else:
                    btn = tk.Button(self, borderwidth=2, relief=tk.GROOVE, font=("Helvetica", 30))
                    btn.place(x=j*width, y=i*width, height=width, width=width)
                    self.slots[i][j] = btn

                if j % 3 == 0 and j != 1:
                    lbl = tk.Label(bg="black")
                    lbl.place(x=j*width, y=0, width=5, height=width*9)

            if i % 3 == 0:
                lbl = tk.Label(bg="black")
                lbl.place(x=0, y=width*i, height=5, width=width*9)

    def is_valid(self, num, pos):
        for i in range(len(self.board)):
            if self.slots[pos[0]][i].cget("text") == num:
                return False
            
        for i in range(len(self.board[0])):
            if self.slots[i][pos[1]].cget("text") == num:
                return False

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.slots[i][j].cget("text") == num and (i, j) != pos:
                    return False

        return True


    '''def btn_press(self, e):
        if not self.selected:
            self.selected = True
            print("Yes", e.widget)
            e.widget.config(text="1")'''

    def find_empty(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                btn = self.slots[i][j]
                if btn.cget("text") == "":
                    return(i, j)
        
        return None


if __name__ == '__main__':
    app = Board(board)
