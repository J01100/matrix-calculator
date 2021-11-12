from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
import numpy as np
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Add:
    def back_to_menu(self):
        self.gui_add_output.destroy()
        menu.gui_menu.deiconify()

    def compute_sum(self):
        try:
            for i in range(self.rows_get):
                for j in range(self.cols_get):
                    self.matrix_a[i][j] = int(self.matrix_a[i][j])

            for i in range(self.rows_get):
                for j in range(self.cols_get):
                    self.matrix_b[i][j] = int(self.matrix_b[i][j])

            self.sum_matrix = np.add(self.matrix_a, self.matrix_b)
            print(self.sum_matrix)
        except TypeError or Exception:
            pass

        try:
            list_mat = [str(i) for i in self.sum_matrix]

            # remove square brackets
            for i in range(len(list_mat)):
                list_mat[i] = list_mat[i][1:-1]
            return list_mat

        except NameError or TypeError or Exception:
            pass

    def output_matrix(self):
        self.gui_add_input.destroy()
        self.gui_add_output = Toplevel()
        self.gui_add_output.title("Add")
        self.gui_add_output.resizable(False, False)

        self.frame_add_output = Frame(self.gui_add_output, highlightbackground='black', highlightthickness=1)
        self.frame_add_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # go back to menu button
        Button(self.frame_add_output, text="Back", width=4, command=self.back_to_menu).grid(
            row=self.rows_get + self.rows_get + 10,
            column=1)

        Label(self.frame_add_output, text='Matrix A:', font=('arial', 10, 'bold'), underline=0).grid(row=1, column=1)
        for i in range(self.rows_get):
            for j in range(self.cols_get):
                Label(self.frame_add_output, text=self.matrix_a[i][j], bd=5).grid(row=i+1, column=j+2)

        Label(self.frame_add_output, text='Matrix B:', font=('arial', 10, 'bold'), underline=0)\
            .grid(row=1, column=self.cols_get+2)
        for i in range(self.rows_get):
            for j in range(self.cols_get):
                Label(self.frame_add_output, text=self.matrix_b[i][j], bd=5).grid(row=i+1, column=j+self.cols_get*2+2)

        #display output
        Label(self.frame_add_output, text='Output:', font=('arial', 10, 'bold'), underline=0).grid(
            row=self.rows_get * 2,
            column=1)

        self.sum_matrix = self.compute_sum()
        for i in range(len(self.sum_matrix)):
            Label(self.frame_add_output, text=self.sum_matrix[i], bd=5).grid(
                row=i + self.rows_get * 2, column=2, columnspan=5, sticky='w  ')

        self.gui_add_output.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_add_output.mainloop()

    def input_matrix(self):
        self.gui_add_menu.destroy()
        self.gui_add_input = Toplevel()
        self.gui_add_input.title("Add")
        self.gui_add_input.resizable(False, False)

        self.frame_add_input = Frame(self.gui_add_input, highlightbackground='black', highlightthickness=1)
        self.frame_add_input.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_add_input, text="Enter matrix A:", font=('arial', 10, 'bold')).grid(row=1, column=1)

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
                    Label(self.frame_add_input, text=alphabet[j]).grid(row=1, column=j + 2)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.frame_add_input, textvariable=text_var[i][j], width=3))

                # display entry
                entries[i][j].grid(row=i + 2, column=j + 2)

                # for row indications
                Label(self.frame_add_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        Label(self.frame_add_input, text="Enter matrix B:", font=('arial', 10, 'bold')).grid(row=self.rows_get * 2,
                                                                                             column=1)
        text_var_b = []
        entries_b = []

        for i in range(self.rows_get):
            # append an empty list to arrays to append to later
            text_var_b.append([])
            entries_b.append([])
            for j in range(self.cols_get):
                # for column indications
                if i == 1:
                    Label(self.frame_add_input, text=alphabet[j]).grid(row=self.rows_get * 2, column=j + 2)

                # append StringVar
                text_var_b[i].append(StringVar())

                # append the entry into the list
                entries_b[i].append(Entry(self.frame_add_input, textvariable=text_var_b[i][j], width=3))

                # display entry
                entries_b[i][j].grid(row=i + self.rows_get + 5, column=j + 2)

                # for row indications
                Label(self.frame_add_input, text=i + 1).grid(row=i + self.rows_get + 5, column=1, sticky='e')

        def get_mat_a():
            self.matrix_a = []
            for i2 in range(self.rows_get):
                self.matrix_a.append([])
                for j2 in range(self.cols_get):
                    self.matrix_a[i2].append(text_var[i2][j2].get())

        def get_mat_b():
            self.matrix_b = []
            for i3 in range(self.rows_get):
                self.matrix_b.append([])
                for j3 in range(self.cols_get):
                    self.matrix_b[i3].append(text_var_b[i3][j3].get())

        def get_mat():
            try:
                get_mat_a()
                get_mat_b()
                self.output_matrix()
            except ValueError or Exception:
                pass

        Button(self.frame_add_input, text="Enter", width=8, command=get_mat)\
            .grid(row=self.cols_get + self.cols_get + 10, column=1)

        self.gui_add_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_add_input.mainloop()

    def __init__(self):
        self.gui_add_input = None
        self.frame_add_input = None
        self.rows_get, self.cols_get = None, None
        self.matrix_a, self.matrix_b = None, None
        self.gui_add_output = None
        self.frame_add_output = None
        self.sum_matrix = None

        menu.gui_menu.withdraw()
        self.gui_add_menu = Toplevel()
        self.gui_add_menu.title("Multiply")
        self.gui_add_menu.resizable(False, False)

        self.frame_add_menu = Frame(self.gui_add_menu, highlightbackground='black', highlightthickness=1)
        self.frame_add_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_add_menu, text='Matrix dimensions:', font=('arial', 10, 'bold'))\
            .grid(row=3, column=1, columnspan=1)

        self.rows = IntVar()
        self.rows.set(2)
        OptionMenu(self.frame_add_menu, self.rows, *range(2, 5)).grid(row=3, column=2)

        Label(self.frame_add_menu, text='x').grid(row=3, column=3)

        self.cols = IntVar()
        self.cols.set(2)
        OptionMenu(self.frame_add_menu, self.cols, *range(2, 5)).grid(row=3, column=4)

        Button(self.frame_add_menu, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=5, column=4)

        self.gui_add_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_add_menu.mainloop()
