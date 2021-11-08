from tkinter import Tk, Label, Button
import inverse 


gui_menu = Tk()
gui_menu.geometry('150x180')
gui_menu.title('Menu')
class Menu:
    def __init__(self):
        label = Label(gui_menu, text="Choose Operation:", pady=10, font=('arial', 10, 'bold'))

        inv = Button(text="Inverse", padx=30, pady=5, command=inverse.Inverse) 
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