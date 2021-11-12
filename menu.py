from tkinter import Tk, Label, Button, Frame
from tkinter.constants import BOTH
import inverse
import multi
import trans
import add

gui_menu = Tk()
# gui_menu.geometry('150x180')
gui_menu.title('Menu')
gui_menu.resizable(False, False)
frame_menu = Frame(gui_menu, highlightbackground='black', highlightthickness=1)
frame_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)


class Menu:
    def __init__(self):
        label = Label(frame_menu, text="Choose Operation:", pady=10, font=('arial', 10, 'bold'))

        inv = Button(frame_menu, text="Inverse", padx=30, pady=5, command=inverse.Inverse)
        ad = Button(frame_menu, text="Add", padx=40, pady=5, command=add.Add)
        tran = Button(frame_menu, text="Transpose", padx=22, pady=5, command=trans.Trans)
        mlt = Button(frame_menu, text="Multiply", padx=28, pady=5, command=multi.Multi)

        label.pack()
        inv.pack()
        mlt.pack()
        ad.pack()
        tran.pack()

        # def on_closing():
        #      if messagebox.askokcancel("Quit", "Do you want to quit?"):
        #         gui_menu.destroy()
        # gui_menu.protocol("WM_DELETE_WINDOW", on_closing)

        gui_menu.mainloop()
