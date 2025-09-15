from tkinter import *

# Main window
window = Tk()
window.geometry("350x500")
window.config(bg="#1e1e1e")
window.title("Modern Calculator")

# Entry field (Display)
e = Entry(window, width=20, borderwidth=8, font=("Arial", 24), bg="#2d2d2d", fg="white", justify="right")
e.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Global variables
math = ""
i = 0

# Function for numbers
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Operation functions
def set_operation(operation):
    global i, math
    i = float(e.get())
    math = operation
    e.delete(0, END)

def equal():
    n2 = e.get()
    e.delete(0, END)
    try:
        n2 = float(n2)
        if math == 'addition':
            e.insert(0, i + n2)
        elif math == 'subtraction':
            e.insert(0, i - n2)
        elif math == 'multiplication':
            e.insert(0, i * n2)
        elif math == 'division':
            e.insert(0, i / n2 if n2 != 0 else "Error")
    except:
        e.insert(0, "Error")

def clean():
    e.delete(0, END)

# Button Style
btn_style = {"font": ("Arial", 16), "width": 5, "height": 2, "bd": 0, "relief": "flat"}

# Button Colors
def create_btn(text, row, col, cmd=None, bg="#3a3a3a", fg="white"):
    return Button(window, text=text, **btn_style, bg=bg, fg=fg,
                  activebackground="#5a5a5a", activeforeground="white",
                  command=cmd).grid(row=row, column=col, padx=5, pady=5)

# Number buttons
numbers = [
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (0, 4, 1)
]

for num, r, c in numbers:
    create_btn(str(num), r, c, lambda n=num: click(n))

# Operators
create_btn("+", 1, 3, lambda: set_operation("addition"), bg="#ff9500")
create_btn("-", 2, 3, lambda: set_operation("subtraction"), bg="#ff9500")
create_btn("*", 3, 3, lambda: set_operation("multiplication"), bg="#ff9500")
create_btn("/", 4, 3, lambda: set_operation("division"), bg="#ff9500")
create_btn("=", 4, 2, equal, bg="#34c759")
create_btn("C", 4, 0, clean, bg="#ff3b30")

window.mainloop()
