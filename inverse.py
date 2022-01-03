from tkinter import Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame, Toplevel
from tkinter.constants import BOTH
from numpy.linalg import inv
import menu

alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Inverse:
    def back_to_menu(self):
        self.gui_inverse_output.destroy()
        menu.gui_menu.deiconify()

    def compute_inverse(self):
        # convert matrix of strings to integers
        try:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = int(self.matrix[i][j])

        except (NameError, TypeError, Exception):
            # Label(self.frame_inverse_output, text="Invalid input(s)").grid(row=1, column=2)
            pass

        try:
            # invert matrix then convert back to string
            self.matrix = inv(self.matrix)
            list_mat = [str(i) for i in self.matrix]

            # remove square brackets
            for i in range(len(list_mat)):
                list_mat[i] = list_mat[i][1:-1]
            return list_mat

        except (TypeError, Exception):
            Label(self.frame_inverse_output, text="(Your matrix is").grid(row=1, column=self.cols * 2 + 1)
            Label(self.frame_inverse_output, text="not invertible!)").grid(row=2, column=self.cols * 2 + 1)

    def output_matrix(self):
        # create window
        self.gui_inverse_input.destroy()
        self.gui_inverse_output = Toplevel()
        self.gui_inverse_output.title("Inverse")
        self.gui_inverse_output.resizable(False, False)

        self.frame_inverse_output = Frame(self.gui_inverse_output, highlightbackground='black', highlightthickness=1)
        self.frame_inverse_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # go back to menu button
        Button(self.frame_inverse_output, text="Back", width=4, command=self.back_to_menu).grid(
            row=self.rows + 10,
            column=1)

        # display user input
        Label(self.frame_inverse_output, text='Input:', font=('arial', 10, 'bold'), underline=0).grid(row=1, column=1)
        for i in range(self.rows):
            for j in range(self.cols):
                Label(self.frame_inverse_output, text=self.matrix[i][j], bd=5).grid(row=i + 1, column=j + 2)

        # display output
        Label(self.frame_inverse_output, text='Inverted:', font=('arial', 10, 'bold'), underline=0).grid(row=1,
                                                                                                       column=self.cols * 2)

        inverse_matrix = self.compute_inverse()
        for i in range(self.rows):
            Label(self.frame_inverse_output, text=inverse_matrix[i], bd=5).grid(
                row=i + 1, column=self.cols * 2 + 1)

        # def disable_event():
        #    pass

        self.gui_inverse_output.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_inverse_output.mainloop()

    def input_matrix(self):
        self.gui_inverse_menu.destroy()
        self.gui_inverse_input = Toplevel()
        self.gui_inverse_input.title("Inverse")
        self.gui_inverse_input.resizable(False, False)

        self.frame_inverse_input = Frame(self.gui_inverse_input, highlightbackground='black', highlightthickness=1)
        self.frame_inverse_input.pack(fill=BOTH, expand=True, padx=5, pady=5)
        # window_dimensions = str(self.m_length.get()**3+90) + "x" + str(self.m_height.get())
        # print(window_dimensions)
        # window.geometry(window_dimensions)
        # self.gui_inverse_input.resizable(False, False)

        Label(self.frame_inverse_input, text="Enter matrix:", font=('arial', 10, 'bold')).grid(row=1, column=1)

        # to create matrix of entry cells we need to create a 2d list of entries
        # thank god to stackoverflow peeps for that

        # empty arrays for Entry and StringVars
        text_var = []
        entries = []

        self.rows, self.cols = (self.m_dimensions.get(), self.m_dimensions.get())
        for i in range(self.rows):
            # append an empty list to arrays to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols):
                # for column indications
                if i == 1:
                    Label(self.frame_inverse_input, text=alphabet[j]).grid(row=1, column=j + 2)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.frame_inverse_input, textvariable=text_var[i][j], width=3))

                # display entry
                entries[i][j].grid(row=i + 2, column=j + 2)

                # for row indications
                Label(self.frame_inverse_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        # callback function to get StringVars/convert them to strings
        # and store in matrix[]

        def get_mat():
            try:
                self.matrix = []
                for i2 in range(self.rows):
                    self.matrix.append([])
                    for j2 in range(self.cols):
                        self.matrix[i2].append(text_var[i2][j2].get())
                self.output_matrix()

            except (ValueError, Exception):
                # Label(self.frame_inverse_output, text="Invalid input(s)").grid(row=1, column=2)
                Label(self.frame_inverse_output, text="(Your matrix is").grid(row=1, column=self.cols * 2 + 1)
                Label(self.frame_inverse_output, text="not invertible!)").grid(row=2, column=self.cols * 2 + 1)

        Button(self.frame_inverse_input, text="Enter", width=8, command=get_mat).grid(row=self.cols + 10,
                                                                                      column=1)

        self.gui_inverse_input.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_inverse_input.mainloop()

    def __init__(self):
        self.gui_inverse_input, self.gui_inverse_output = None, None
        self.frame_inverse_output, self.frame_inverse_input = None, None
        self.frame_inverse_menu = None
        self.inverse_matrix = []
        self.rows, self.cols = None, None
        self.matrix = None

        menu.gui_menu.withdraw()
        self.gui_inverse_menu = Toplevel()
        self.gui_inverse_menu.title("Inverse")
        self.gui_inverse_menu.resizable(False, False)

        self.frame_inverse_menu = Frame(self.gui_inverse_menu, highlightbackground='black', highlightthickness=1)
        self.frame_inverse_menu.pack(fill=BOTH, expand=True, padx=5, pady=5)

        Label(self.frame_inverse_menu, text='Enter matrix dimensions:', font=('arial', 10, 'bold')).grid(row=4, column=1)

        # enter matrix dimensions
        self.m_dimensions = IntVar()
        self.m_dimensions.set(2)
        OptionMenu(self.frame_inverse_menu, self.m_dimensions, *range(2, 5)).grid(row=4, column=2)

        Button(self.frame_inverse_menu, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=5, column=2)

        self.gui_inverse_menu.protocol("WM_DELETE_WINDOW", menu.gui_menu.destroy)
        self.gui_inverse_menu.mainloop()
