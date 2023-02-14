from tkinter import *
import random, sys
from tkinter import messagebox
import time

game_state = True
number = random.sample(range(1,100), 30)


def click(row, column):
    
    
    if str(buttons[row][column]["text"]) != number_lbl.cget("text"):
        messagebox.showerror("Error", "Wrong number")
    else:

        buttons[row][column].config(state="disabled")
        matrix_state[row][column] =  "clear"
        
        check_row(matrix_state, row)
        check_col(matrix_state, column)
        check_diagonal(matrix_state)
        
        
    
def check_row(matrix_stage, row):
    
    if matrix_stage[row][0] == "clear" and matrix_stage[row][1] == "clear" and matrix_stage[row][2] == "clear":
        messagebox.showinfo("Info", "BINGO")
        window.quit()
           
def check_col(matrix_stage, col):
    
    if matrix_stage[0][col] == "clear" and matrix_stage[1][col] == "clear" and matrix_stage[2][col] == "clear" :
        messagebox.showinfo("Info", "BINGO")
        window.quit()
    
def check_diagonal(matrix_stage):
    
    if matrix_stage[0][0] == "clear" and  matrix_stage[1][1] == "clear" and matrix_stage[2][2] == "clear":
        messagebox.showinfo("Info", "BINGO")
        window.quit()
    elif matrix_stage[2][0] == "clear" and  matrix_stage[1][1] == "clear" and matrix_stage[0][2] == "clear":
        messagebox.showinfo("Info", "BINGO")
        window.quit()

def update_number():
    
    number_lst = number
    
    lbl_var.set(str(number_lst[random.randint(0, 29)]))
    number_lbl.after(3000, update_number)
    


window = Tk()
window.geometry("400x300")
window.title("BINGO GAME")

lbl_var = StringVar()

number_lbl = Label(
    window,
    font=18,
    text="",
    textvariable=lbl_var
)

number_lbl.place(x=250, y=85)

frame = Frame(window).grid(row=2, column=0)


update_number()

buttons = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

matrix_state = [
    ["","",""],
    ["","",""],
    ["","",""]
]

for i in range(3):
    for j in range(3):
        num = number[random.randint(0, 29)]
        buttons[i][j] = Button(
            frame,
            text=num,
            font=14,
            width=2,
            command=lambda row=i, column=j: click(row,column)
        )
        buttons[i][j].grid(row=i, column=j, padx=10, pady=10)

window.mainloop()