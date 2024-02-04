
import tkinter as tk 
from tkinter import *
def display_and_update_graphical_grid(game_grid):
    window= tk.Tk()
    window.title("2048")
    toplevel = Toplevel(window)
    toplevel.title("2048")
    toplevel.grid()
    for row1 in range(len(game_grid)):
        for col in range(len(game_grid)):
            if game_grid[row1][col]== 0:
                cell=Frame(toplevel,width=50,height=50,bg="grey",relief="solid",bd=0.5)
                cell.grid(row=row1,column=col)
            else:
                cell=Frame(toplevel,width=50,height=50,bg="beige",relief="solid")
                label= Label(cell, text=str(game_grid[row1][col]))
                label.pack(expand=True)
                cell.grid(row=row1,column=col)
    window.mainloop()
    toplevel.mainloop()

game_grid=[[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2], [0, 0, 0, 0]]
display_and_update_graphical_grid(game_grid)








