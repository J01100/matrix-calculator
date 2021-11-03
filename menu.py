from tkinter import *



class Menu:
    def __init__(self):
        menu = Tk(className="Mtx Operations")
        menu.geometry("150x180")
        # menu['background'] = '#121212' # crappy

        # create label
        text = Label(menu, text="Choose Operation:", pady=10)

        inv = Button(menu, text="Inverse", padx=30, pady=5)
        add = Button(menu, text="Add", padx=40, pady=5)
        sub = Button(menu, text="Subtract", padx=25, pady=5)
        mlt = Button(menu, text="Multiply", padx=28, pady=5)

        text.pack()
        inv.pack()
        add.pack()
        sub.pack()
        mlt.pack()

        # run window
        menu.mainloop()

        # a = Matrix(inp_length(), inp_height())
        # a.enter_values()
        # a.print_matrix()
