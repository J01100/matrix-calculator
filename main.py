import numpy as np
import sympy as sp
from tkinter import *
from IPython.display import display, Math
from matrix import *


def main():
    window = Tk()

    # create objects
    label = Label(window, text="Matrix Operations")
    label2 = Label(window, text="Choose operation:")

    add_matrix = Button(window, text="button")
    sub_matrix = Button(window, text="button")
    mlt_matrix = Button(window, text="button")

    # show objects in screen
    label.pack()
    label2.pack()
    add_matrix.pack()
    sub_matrix.pack()
    mlt_matrix.pack()

    # run window
    window.mainloop()


# a = Matrix(inp_length(), inp_height())
# a.enter_values()
# a.print_matrix()


if __name__ == '__main__':
    main()
