import menu
from menu import *
from tkinter import *

# to fix, destroy inverse_dimensions_menu after entering dimensions (i think it is better to create 1 class per window)
# figure out how to record the entry values to print the matrix and do the operations.
# print the input matrix and the output matrix


def inverse_dimensions_menu():
    menu.gui_menu.destroy()
    inverse_wdw = Tk(className='MtxOp')
    # inverse_wdw.geometry('150x100')
    # enter matrix length
    Label(inverse_wdw, text='Inverse of a Matrix').grid(row=1, column=1)
    Label(inverse_wdw, text='Enter matrix length:').grid(row=3, column=1)
    # enter matrix height
    Label(inverse_wdw, text='Enter matrix height:').grid(row=4, column=1)
    # store dimensions
    m_length = IntVar()
    m_height = IntVar()
    m_length.set(2)
    m_height.set(2)

    OptionMenu(inverse_wdw, m_length, *range(1, 11)).grid(row=3, column=2)
    OptionMenu(inverse_wdw, m_height, *range(1, 11)).grid(row=4, column=2)

    # Entry(inverse_wdw, textvariable=m_length, justify=RIGHT, width=2).grid(row=3, column=2)
    # Entry(inverse_wdw, textvariable=m_height, justify=RIGHT, width=2).grid(row=4, column=2)

    def inverse_input():
        # create array storage based on dimensions
        arr = []
        for i in range(m_height.get()):
            temp = []
            for j in range(m_length.get()):
                temp.append(j)
            arr.append(temp)

        # create entries and store into array storage
        Label(inverse_wdw, text='Enter matrix elements:').grid(row=1, column=3)
        for i in range(m_height.get()):
            for j in range(m_length.get()):
                if i == 1:
                    Label(inverse_wdw, text=j + 1).grid(row=1, column=j+4)
                Entry(inverse_wdw, textvariable=arr[i][j], width=2).grid(row=i+3, column=j+4)
            Label(inverse_wdw, text=i+1).grid(row=i+3, column=3, sticky='e')

    Button(inverse_wdw, text='Enter', padx=16, pady=5, command=inverse_input).grid(row=5, column=2)

    # POSSIBLE CAUSES OF ERROR; wrong input data type, :window, tkinter, there is nolength and height limit. if
    # length/height too high print invalid
    inverse_wdw.mainloop()


class Inverse:
    def __init__(self):
        pass
