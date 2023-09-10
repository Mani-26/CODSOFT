import pyperclip
import random
from tkinter import *
from tkinter.ttk import *


def low():
    entry.delete(0, END)

    length = var1.get()

    low = "abcdefghijklmnopqrstuvwxyz"
    medium = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    strong = "ABCDEFGHIJKLMNOPQRSTUVWXYZ !@#$%^&*()_abcdefghijklmnopqrstuvwxyz-0123456789"
    password = ""

    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(low)
        return password

    elif var.get() == 2:
        for i in range(0, length):
            password = password + random.choice(medium)
        return password

    elif var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(strong)
        return password


def generate():
    password1 = low()
    entry.insert(10, password1)


def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)


root = Tk()
var = IntVar()
var1 = IntVar()

root.title("Mani's Random Password Generator")

Random_password = Label(root, text="Password")
Random_password.grid(row=0, column=0, padx=10)
entry = Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

c_label = Label(root, text="Length")
c_label.grid(row=2)

copy_button = Button(root, text="Copy", command=copy1)
copy_button.grid(row=1, column=0, padx=20, pady=5)
generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=1, column=1, padx=20)


combo = Combobox(root, textvariable=var1)

combo["values"] = (
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
)
combo.current(0)
combo.bind("<<ComboboxSelected>>")
combo.grid(column=1, row=2, padx=20, pady=10)

radio_low = Radiobutton(root, text="Low", variable=var, value=1)
radio_low.grid(row=0, column=2, sticky="E", padx=25)
radio_middle = Radiobutton(root, text="Medium", variable=var, value=2)
radio_middle.grid(row=1, column=2, sticky="E", padx=2)
radio_strong = Radiobutton(root, text="Strong", variable=var, value=3)
radio_strong.grid(row=2, column=2, sticky="E", padx=10)

root.mainloop()
