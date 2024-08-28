from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)

class gamebaord:
    def __init__(self) -> None:
        self.gb =  []
    
    def __str__(self) -> str:
        return str(self.gb)

def update_button(event):
    # print(event)
    # print(event.window())
    button = event.widget
    grid_info = button.grid_info()
    grid_row = grid_info['row']
    grid_column = grid_info['column']
    ttk.Button(frm, text="x").grid(column=grid_column, row=grid_row)

def fillGameboard(gb):
    for row_num, row in enumerate(gb.gb):
        for col_num, col in enumerate(row):
            gb.gb[row_num][col_num] = ttk.Button(frm, text="")
            gb.gb[row_num][col_num].grid(column=col_num, row=row_num)
            gb.gb[row_num][col_num].bind("<ButtonPress-1>", update_button)

gb1 = gamebaord()
fillGameboard(gb1)

print(gb1)
# print(gb1.gb)
root.mainloop()
print(gb1)