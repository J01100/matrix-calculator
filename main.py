import numpy as np
import sympy as sp
from tkinter import *
from IPython.display import display, Math
from input import *
from matrix import *


def main():
    window = Tk()

    # create objects
    label = Label(window, text="Matrix Operations")
    text = Text(window, cnf={'bg': 'blue'})
    button = Button(window, text="button")

    # show objects in screen
    label.pack()
    text.pack()
    button.pack()

    # run window
    window.mainloop()

# a = Matrix(inp_length(), inp_height())
# a.enter_values()
# a.print_matrix()


if __name__ == '__main__':
    main()
