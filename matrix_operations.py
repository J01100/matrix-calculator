from tkinter import *


class MatrixOperations:
    def __init__(self):
        window1 = Tk(className="Mtx Operations")
        window1.geometry("150x180")
        # window1['background'] = '#121212'

        # create label
        text = Label(window1, text="Choose Operation:", pady=10)

        inv = Button(window1, text="Inverse", padx=30, pady=5)
        add = Button(window1, text="Add", padx=40, pady=5)
        sub = Button(window1, text="Subtract", padx=25, pady=5)
        mlt = Button(window1, text="Multiply", padx=28, pady=5)

        text.pack()
        inv.pack()
        add.pack()
        sub.pack()
        mlt.pack()

        # run window
        window1.mainloop()

        # a = Matrix(inp_length(), inp_height())
        # a.enter_values()
        # a.print_matrix()
