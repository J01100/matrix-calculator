from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Multi:
    def back_to_menu(self):
        self.gui_multi_output.destroy()
        menu.gui_menu.deiconify()

    def compute_inverse(self):
        # convert matrix of strings to integers
        try:
            for i in range(self.rows_a):
                for j in range(self.cols_a):
                    self.matrix[i][j] = int(self.matrix[i][j])

        except NameError or TypeError or Exception:
            Label(self.frame_multi_output, text="Invalid input(s)").grid(row=1, column=2)

        try:
            # invert matrix then convert back to string
            # self.matrix = inv(self.matrix)
            list_mat = [str(i) for i in self.matrix]

            # remove square brackets
            for i in range(len(list_mat)):
                list_mat[i] = list_mat[i][1:-1]
            return list_mat

        except TypeError or Exception:
            Label(self.frame_multi_output, text="(Your matrix is").grid(row=1, column=self.cols_a * 2 + 1)
            Label(self.frame_multi_output, text="not invertible!)").grid(row=2, column=self.cols_a * 2 + 1)

    def output_matrix(self):
        # create window
        self.gui_multi_input.destroy()
        self.gui_multi_output = Toplevel()
        self.gui_multi_output.title("Inverse")
        self.gui_multi_output.resizable(False, False)

        self.frame_multi_output = Frame(self.gui_multi_output, highlightbackground='black', highlightthickness=1)
        self.frame_multi_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # go back to menu button
        Button(self.frame_multi_output, text="Back", width=4, command=self.back_to_menu).grid(
            row=self.rows_a + 10,
            column=1)

        # display user input
        Label(self.frame_multi_output, text='Input:', font=('arial', 10, 'bold'), underline=0).grid(row=1, column=1)
        for i in range(self.rows_a):
            for j in range(self.cols_a):
                Label(self.frame_multi_output, text=self.matrix[i][j], bd=5).grid(row=i + 1, column=j + 2)

        # display output
        Label(self.frame_multi_output, text='Output:', font=('arial', 10, 'bold'), underline=0).grid(row=1,
                                                                                                     column=self.cols_a * 2)

        inverse_matrix = self.compute_inverse()
        for i in range(self.rows_a):
            Label(self.frame_multi_output, text=inverse_matrix[i], bd=5).grid(
                row=i + 1, column=self.cols_a * 2 + 1)

        # def disable_event():
        #    pass

        self.gui_multi_output.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_output.mainloop()

    def input_matrix(self):
        self.gui_multi_menu.destroy()
        self.gui_multi_input = Toplevel()
        self.gui_multi_input.title("Inverse")
        self.gui_multi_input.resizable(False, False)

        self.frame_multi_input = Frame(self.gui_multi_input, highlightbackground='black', highlightthickness=1)
        self.frame_multi_input.pack(fill=BOTH, expand=True, padx=5, pady=5)
        # window_dimensions = str(self.m_length.get()**3+90) + "x" + str(self.m_height.get())
        # print(window_dimensions)
        # window.geometry(window_dimensions)
        # self.gui_inverse_input.resizable(False, False)

        Label(self.frame_multi_input, text="Enter matrix:", font=('arial', 10, 'bold')).grid(row=1, column=1)

        # to create matrix of entry cells we need to create a 2d list of entries
        # thank god to stackoverflow peeps for that

        # empty arrays for Entry and StringVars
        text_var = []
        entries = []

        self.rows_a, self.cols_a = (self.ma_rows.get(), self.ma_cols.get())
        for i in range(self.rows_a):
            # append an empty list to arrays to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols_a):
                # for column indications
                if i == 1:
                    Label(self.frame_multi_input, text=alphabet[j]).grid(row=1, column=j + 2)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.frame_multi_input, textvariable=text_var[i][j], width=3))

                # display entry
                entries[i][j].grid(row=i + 2, column=j + 2)

                # for row indications
                Label(self.frame_multi_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        # callback function to get StringVars/convert them to strings
        # and store in matrix[]

        def get_mat():
            try:
                self.matrix = []
                for i2 in range(self.rows_a):
                    self.matrix.append([])
                    for j2 in range(self.cols_a):
                        self.matrix[i2].append(text_var[i2][j2].get())
                self.output_matrix()

            except ValueError or Exception:
                Label(self.frame_multi_output, text="Invalid input(s)").grid(row=1, column=2)
                Label(self.frame_multi_output, text="(Your matrix is").grid(row=1, column=self.cols_a * 2 + 1)
                Label(self.frame_multi_output, text="not invertible!)").grid(row=2, column=self.cols_a * 2 + 1)

        Button(self.frame_multi_input, text="Enter", width=8, command=get_mat).grid(row=self.cols_a + 10,
                                                                                     column=1)

        self.gui_multi_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_input.mainloop()

    def __init__(self):
        self.matrix = None
        self.gui_multi_input = None
        self.frame_multi_input = None
        self.rows_a, self.cols_a = None, None
        self.gui_multi_output = None
        self.frame_multi_output = None

        menu.gui_menu.withdraw()
        self.gui_multi_menu = Toplevel()
        self.gui_multi_menu.title("Multiply")
        self.gui_multi_menu.resizable(False, False)

        self.frame_multi_menu = Frame(self.gui_multi_menu, highlightbackground='black', highlightthickness=1)
        self.frame_multi_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # inputs
        # Label(self.frame_multi_menu, text='NOTE: Matrix A height and Matrix B length').grid(row=1, column=1, columnspan=6)
        # Label(self.frame_multi_menu, text='...are to be equal for multiplication').grid(row=2, column=1, columnspan=6)
        # A matrix
        Label(self.frame_multi_menu, text='Matrix A dimensions:', font=('arial', 10, 'bold')).grid(row=3, column=1,
                                                                                                   columnspan=1)
        Label(self.frame_multi_menu, text='Matrix B dimensions:', font=('arial', 10, 'bold')).grid(row=4, column=1,
                                                                                                   columnspan=1)

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

        Button(self.frame_multi_menu, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=5, column=4)

        self.gui_multi_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_multi_menu.mainloop()
