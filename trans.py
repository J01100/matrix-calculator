from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
import numpy as np
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Trans:
    def back_to_menu(self):
        self.gui_trans_output.destroy()
        menu.gui_menu.deiconify()

    def compute_transpose(self):
        try:
            for i in range(self.rows_get):
                for j in range(self.cols_get):
                    self.matrix[i][j] = int(self.matrix[i][j])

            list_mat = [str(i) for i in np.transpose(self.matrix)]

            # remove square brackets
            for i in range(len(list_mat)):
                list_mat[i] = list_mat[i][1:-1]
            return list_mat

        except (TypeError, Exception):
            pass

    def output_matrix(self):
        self.gui_trans_input.destroy()
        self.gui_trans_output = Toplevel()
        self.gui_trans_output.title("Transpose")
        self.gui_trans_output.resizable(False, False)

        self.frame_trans_output = Frame(self.gui_trans_output, highlightbackground='black', highlightthickness=1)
        self.frame_trans_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # go back to menu button
        Button(self.frame_trans_output, text="Back", width=4, command=self.back_to_menu).grid(
            row=self.rows_get + self.rows_get + 10, column=1)

        Label(self.frame_trans_output, text='Input:', font=('arial', 10, 'bold'), underline=0).grid(row=1, column=1)
        for i in range(self.rows_get):
            for j in range(self.cols_get):
                Label(self.frame_trans_output, text=self.matrix[i][j], bd=5).grid(row=i + 1, column=j + 2)

        # display output
        Label(self.frame_trans_output, text='Transposed:', font=('arial', 10, 'bold'), underline=0).grid(
            row=self.rows_get * 2,
            column=1)

        self.transposed_matrix = self.compute_transpose()
        for i in range(self.cols_get):
            Label(self.frame_trans_output, text=self.transposed_matrix[i], bd=5).grid(
                row=i + self.rows_get * 2, column=2, columnspan=self.cols_get, sticky='w ')

        self.gui_trans_output.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_output.mainloop()

    def input_matrix(self):
        self.gui_trans_menu.destroy()
        self.gui_trans_input = Toplevel()
        self.gui_trans_input.title("Transpose")
        self.gui_trans_input.resizable(False, False)

        self.frame_trans_input = Frame(self.gui_trans_input, highlightbackground='black', highlightthickness=1)
        self.frame_trans_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_trans_input, text="Enter matrix:", font=('arial', 10, 'bold')).grid(row=1, column=1)

        # empty arrays for Entry and StringVars
        text_var = []
        entries = []

        self.rows_get, self.cols_get = (self.rows.get(), self.cols.get())
        for i in range(self.rows_get):
            # append an empty list to arrays to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols_get):
                # for column indications
                if i == 1:
                    Label(self.frame_trans_input, text=alphabet[j]).grid(row=1, column=j + 2)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.frame_trans_input, textvariable=text_var[i][j], width=3))

                # display entry
                entries[i][j].grid(row=i + 2, column=j + 2)

                # for row indications
                Label(self.frame_trans_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        def get_mat():
            try:
                self.matrix = []
                for i2 in range(self.rows_get):
                    self.matrix.append([])
                    for j2 in range(self.cols_get):
                        self.matrix[i2].append(text_var[i2][j2].get())
                self.output_matrix()
            except (ValueError, Exception):
                pass

        Button(self.frame_trans_input, text="Enter", width=8, command=get_mat)\
            .grid(row=self.cols_get + self.cols_get + 10, column=1)

        self.gui_trans_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_input.mainloop()

    def __init__(self):
        self.gui_trans_input = None
        self.frame_trans_input = None
        self.gui_trans_output = None
        self.frame_trans_output = None
        self.transposed_matrix = None
        self.matrix = None
        self.rows_get, self.cols_get = None, None

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

        Button(self.frame_trans_menu, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=2, column=4)

        self.gui_trans_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_trans_menu.mainloop()
