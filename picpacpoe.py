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
        return str(self.gb)
    
    def display_current_player(self):
        current_player =tk.Label(master=frame, text=self.current_player)
        current_player.pack()

    def update_button(self, event):
        self.current_player = "x" if self.current_player == "O" else "O"
        button = event.widget
        grid_info = button.grid_info()
        grid_row = grid_info['row']
        grid_column = grid_info['column']
        tk.Button(frame, text=self.current_player).grid(row = grid_row, column = grid_column)
        
window = tk.Tk()

frame = tk.Frame(master=window, padx=20, pady=20)
frame.grid()

gb1 = gamebaord()

for row_num in range(0,3):
    for col_num in range(0,3):
        gb1.gb[row_num][col_num] = tk.Button(master=frame, text="")
        gb1.gb[row_num][col_num].bind("<ButtonPress-1>", gb1.update_button)
        gb1.gb[row_num][col_num].grid(column=col_num, row=row_num)


# button = tk.Button(master=frame)
# button.bind("<ButtonPress-1>", update_button)
# button.pack()

window.mainloop()

