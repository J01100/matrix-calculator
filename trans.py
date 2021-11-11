from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
import numpy as np
import menu


class Trans:
    def __init__(self):
        menu.gui_menu.withdraw()
        self.gui_trans_menu = Toplevel()
        self.gui_trans_menu.title("Transpose")
        self.gui_trans_menu.resizable(False, False)

        self.frame_trans_menu = Frame(self.gui_trans_menu, highlightbackground='black', highlightthicknes=1)
        self.frame_trans_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_trans_menu, text='Enter matrix dimensions:', font=('arial', 10, 'bold')).grid(row=1, column=1)

        # enter matrix dimensions:
        self.rows = IntVar()
        self.rows.set(2)
        OptionMenu(self.frame_trans_menu, self.rows, *range(2, 5)).grid(row=1, column=2)

        Label(self.frame_trans_menu, text='x').grid(row=1, column=3)

        self.cols = IntVar()
        self.cols.set(2)
        OptionMenu(self.frame_trans_menu, self.cols, *range(2, 5)).grid(row=1, column=4)

        Button(self.frame_trans_menu, text='Enter', padx=16, pady=5).grid(row=2, column=4)

        self.gui_trans_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_menu.mainloop()
