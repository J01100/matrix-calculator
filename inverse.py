from tkinter import Tk, Label, Button, Entry, OptionMenu, IntVar, StringVar, Frame
from tkinter.constants import BOTH
from numpy.linalg import inv
import menu


alphabet = 'abcdefghijklmnopqrstuvwxyz'


class Inverse:
    def compute_inverse(self):
        # convert matrix of strings to integers
        try:
            for i in range(self.rows):
                for j in range(self.cols):
                    self.matrix[i][j] = int(self.matrix[i][j])
        except ValueError:
            Label(self.frame_inverse_output, text="Invalid input(s)").grid(row=2, column=1)

        try:
            list_mat = [str(i) for i in (inv(self.matrix))]
            return list_mat
        except Exception:
            Label(self.frame_inverse_output, text="(Your matrix is").grid(row=2, column=self.cols * 2 + 1)
            Label(self.frame_inverse_output, text="not invertible!)").grid(row=3, column=self.cols * 2 + 1)

    def output_matrix(self):
        # create window
        self.gui_inverse_input.destroy()
        self.gui_inverse_output = Tk()
        self.gui_inverse_output.title("Inverse")
        self.gui_inverse_output.resizable(False, False)

        self.frame_inverse_output = Frame(self.gui_inverse_output)
        self.frame_inverse_output.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # display user input
        Label(self.frame_inverse_output, text='Input:', font=('arial', 10, 'bold')).grid(row=1, column=1)
        for i in range(self.rows):
            for j in range(self.cols):
                Label(self.frame_inverse_output, text=self.matrix[i][j], bd=5).grid(row=i + 2, column=j + 2)

        # display output
        if self.cols <= self.rows:
            Label(self.frame_inverse_output, text='Output:', font=('arial', 10, 'bold')).grid(row=1,
                                                                                              column=self.cols * 2)
            for i in range(self.rows):
                for j in range(self.cols):
                    Label(self.frame_inverse_output, text=self.compute_inverse()[i], bd=5).grid(
                        row=i + 2, column=self.cols * 2 + 1)

    def input_matrix(self):
        self.gui_inverse_menu.destroy()
        self.gui_inverse_input = Tk()
        self.gui_inverse_input.title("Inverse")
        self.gui_inverse_input.resizable(False, False)
        # window_dimensions = str(self.m_length.get()**3+90) + "x" + str(self.m_height.get())
        # print(window_dimensions)
        # window.geometry(window_dimensions)
        self.gui_inverse_input.resizable(False, False)

        Label(self.gui_inverse_input, text="Enter matrix:", font=('arial', 10, 'bold')).grid(row=1, column=1)

        # to create matrix of entry cells we need to create a 2d list of entries
        # thank god to stackoverflow peeps for that

        # empty arrays for Entrys and StringVars
        text_var = []
        entries = []

        self.rows, self.cols = (self.m_length.get(), self.m_height.get())
        for i in range(self.rows):
            # append an empty list to arrays to append to later
            text_var.append([])
            entries.append([])
            for j in range(self.cols):
                # for column indications
                if i == 1:
                    Label(self.gui_inverse_input, text=alphabet[j]).grid(row=1, column=j + 2)

                # append StringVar
                text_var[i].append(StringVar())

                # append the entry into the list
                entries[i].append(Entry(self.gui_inverse_input, textvariable=text_var[i][j], width=3))

                # display entry
                entries[i][j].grid(row=i + 2, column=j + 2)

                # for row indications
                Label(self.gui_inverse_input, text=i + 1).grid(row=i + 2, column=1, sticky='e')

        # callback function to get StringVars/convert them to strings
        # and store in matrix[]
        def get_mat():
            self.matrix = []
            for i in range(self.rows):
                self.matrix.append([])
                for j in range(self.cols):
                    self.matrix[i].append(text_var[i][j].get())
            self.output_matrix()

        Button(self.gui_inverse_input, text="Enter", width=8, command=get_mat).grid(row=self.m_height.get() + 10,
                                                                                    column=1)

        self.gui_inverse_input.mainloop()

    def __init__(self):
        self.gui_inverse_input, self.gui_inverse_output = None, None
        self.frame_inverse_output = None
        self.inverse_matrix = []
        self.rows, self.cols = None, None
        self.matrix = None

        menu.gui_menu.destroy()
        self.gui_inverse_menu = Tk()
        self.gui_inverse_menu.title("Inverse")
        self.gui_inverse_menu.resizable(False, False)

        Label(self.gui_inverse_menu, text='Enter matrix length:').grid(row=3, column=1)
        Label(self.gui_inverse_menu, text='Enter matrix height:').grid(row=4, column=1)

        # enter matrix dimensions
        self.m_length = IntVar()
        self.m_height = IntVar()
        self.m_length.set(2)
        self.m_height.set(2)
        OptionMenu(self.gui_inverse_menu, self.m_length, *range(2, 11)).grid(row=3, column=2)
        OptionMenu(self.gui_inverse_menu, self.m_height, *range(2, 11)).grid(row=4, column=2)

        Button(self.gui_inverse_menu, text='Enter', padx=16, pady=5, command=self.input_matrix).grid(row=5, column=2)
