from tkinter import *
from operations import *


gui_menu = Tk(className="Mtx Operations")


class Menu:
    def __init__(self):
        gui_menu.geometry("150x180")
        # gui_menu['background'] = '#121212' # crappy

        # create label
        label = Label(gui_menu, text="Choose Operation:", pady=10)

        inv = Button(gui_menu, text="Inverse", padx=30, pady=5, command=inverse_op)
        add = Button(gui_menu, text="Add", padx=40, pady=5)
        sub = Button(gui_menu, text="Subtract", padx=25, pady=5)
        mlt = Button(gui_menu, text="Multiply", padx=28, pady=5)

        label.pack()
        inv.pack()
        add.pack()
        sub.pack()
        mlt.pack()

        # run window
        gui_menu.mainloop()

        # a = Matrix(inp_length(), inp_height())
        # a.enter_values()
        # a.print_matrix()
