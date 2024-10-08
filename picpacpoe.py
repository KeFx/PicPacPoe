import tkinter as tk
from itertools import cycle
from tkinter import *
from typing import NamedTuple

current_player = "x"

class gamebaord:
    def __init__(self) -> None:
        self.gb =  [['','',''],['','',''],['','','']]
        self.current_player = "x"
    
    def __str__(self) -> str:
        return '\n'.join(['|'.join(row) for row in self.gb])
    
    def process_move(self, event):
        self.set_current_player()
        self.update_cell(event)
        self.check_for_win()

    def set_current_player(self):
        self.current_player = "x" if self.current_player == "O" else "O"

    def update_cell(self, event):
        tkButton = event.widget
        grid_info = tkButton.grid_info()
        row = grid_info['row']
        column = grid_info['column']

        self.update_gb_cell(row, column)
        self.update_tk_button(row, column)

    def update_gb_cell(self, row, column):
        self.gb[row][column] = self.current_player

    def update_tk_button(self, row, column):
        tk.Button(frame, text=self.current_player).grid(row = row, column = column)

    def check_for_win(self):
        if self.row_win() or self.column_win() or self.diagonal_win():
            win_message = tk.Label(text=f"{self.current_player} wins", width=20, borderwidth=1, relief="solid", background="blue")
            win_message.place(relx=1.0, rely=1.0, x=1, y=-40, anchor="se")
    
    def row_win(self):
        for row in self.gb:
            if row[0] != " " and (row[0] == row[1] == row[2]):
               return True
    
    def column_win(self):
        for column in range(0,3):
            if self.gb[0][column] != " " and (self.gb[0][column] == self.gb[1][column] == self.gb[2][column]):
                return True

    def diagonal_win(self):
        postive_diagonal_win = self.gb[0][2] != " " and (self.gb[0][2] == self.gb[1][1] == self.gb[2][0])
        negative_diagonal_win = self.gb[0][0] != " " and (self.gb[0][0] == self.gb[1][1] == self.gb[2][2])

        return postive_diagonal_win or negative_diagonal_win

window = tk.Tk()

frame = tk.Frame(master=window, padx=20, pady=20)
frame.grid()

gb1 = gamebaord()

for row_num in range(0,3):
    for col_num in range(0,3):
        button = tk.Button(master=frame, text=" ")
        button.bind("<ButtonPress-1>", gb1.process_move)
        button.grid(column=col_num, row=row_num)

        gb1.gb[row_num][col_num] = " "

# button = tk.Button(master=frame)
# button.bind("<ButtonPress-1>", update_button)
# button.pack()

window.mainloop()
print(gb1)
