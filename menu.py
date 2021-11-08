from tkinter import Tk, Label, Button, Frame
from tkinter.constants import BOTH
import inverse

gui_menu = Tk()
gui_menu.geometry('150x180')
gui_menu.title('Menu')
frame_menu = Frame(gui_menu, highlightbackground='black', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)


class Menu:
    def __init__(self):
        label = Label(frame_menu, text="Choose Operation:", pady=10, font=('arial', 10, 'bold'))

        inv = Button(frame_menu, text="Inverse", padx=30, pady=5, command=inverse.Inverse)
        add = Button(frame_menu, text="Add", padx=40, pady=5)
        sub = Button(frame_menu, text="Subtract", padx=25, pady=5)
        mlt = Button(frame_menu, text="Multiply", padx=28, pady=5)

        label.pack()
        inv.pack()
        add.pack()
        sub.pack()
        mlt.pack()

        # run window
        gui_menu.mainloop()
