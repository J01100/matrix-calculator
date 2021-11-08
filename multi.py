from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
import menu


class Multi:
    def __init__(self):
        menu.gui_menu.withdraw()
        self.gui_multi_menu = Toplevel()
        self.gui_multi_menu.title("Multiply")
        self.gui_multi_menu.resizable(False, False)

        self.frame_multi_menu = Frame(self.gui_multi_menu, highlightbackground='black', highlightthickness=1)
        self.frame_multi_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # inputs
        Label(self.frame_multi_menu, text='NOTE: Matrix A height and Matrix B length').grid(row=1, column=1, columnspan=6)
        Label(self.frame_multi_menu, text='...are to be equal for multiplication').grid(row=2, column=1, columnspan=6)
        # A matrix
        Label(self.frame_multi_menu, text='Matrix A dimensions:', font=('arial', 10, 'bold')).grid(row=3, column=1, columnspan=1)
        Label(self.frame_multi_menu, text='Matrix B dimensions:', font=('arial', 10, 'bold')).grid(row=4, column=1, columnspan=1)

        self.ma_rows = IntVar()
        self.ma_rows.set(2)
        OptionMenu(self.frame_multi_menu, self.ma_rows, *range(2, 16)).grid(row=3, column=2)

        Label(self.frame_multi_menu, text='x').grid(row=3, column=3)

        self.ma_cols = IntVar()
        self.ma_cols.set(2)
        OptionMenu(self.frame_multi_menu, self.ma_cols, *range(2, 16)).grid(row=3, column=4)

        # B matrix
        self.mb_rows = IntVar()
        self.mb_rows.set(self.ma_cols.get())
        Label(self.frame_multi_menu, text="[n]", font=('arial', 10, 'bold'), padx=5, pady=5).grid(row=4, column=2)
        # OptionMenu(self.frame_multi_menu, self.mb_rows, *range(2, 16)).grid(row=2, column=2)

        Label(self.frame_multi_menu, text='x').grid(row=4, column=3)

        self.mb_cols = IntVar()
        self.mb_cols.set(2)
        OptionMenu(self.frame_multi_menu, self.mb_cols, *range(2, 16)).grid(row=4, column=4)

        Button(self.frame_multi_menu, text='Enter', padx=16, pady=5).grid(row=5, column=4)

        self.gui_multi_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_menu.mainloop()
