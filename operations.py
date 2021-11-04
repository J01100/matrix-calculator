from tkinter import *
from tkinter import ttk
from menu import *
import menu
import sympy as sp

def inverse_op():
    menu.gui_menu.destroy()
    inverse_wdw = Tk(className='MtxOp')
    # inverse_wdw.geometry('150x100')
    # enter matrix length
    Label(inverse_wdw, text='Inverse of a Matrix').grid(row=1, column=1)
    Label(inverse_wdw, text='Enter matrix length:').grid(row=3, column=1)
    # enter matrix height
    Label(inverse_wdw, text='Enter matrix height:').grid(row=4, column=1)
    # store inputs
    m_length = IntVar()
    m_length.set(2)
    m_height = IntVar()
    m_height.set(2)

    OptionMenu(inverse_wdw, m_length, *range(1, 11)).grid(row=3, column=2)
    OptionMenu(inverse_wdw, m_height, *range(1, 11)).grid(row=4, column=2)
    #Entry(inverse_wdw, textvariable=m_length, justify=RIGHT, width=2).grid(row=3, column=2)
    #Entry(inverse_wdw, textvariable=m_height, justify=RIGHT, width=2).grid(row=4, column=2)
    Button(inverse_wdw, text='Enter', padx=16, pady=5).grid(row=5, column=2)


    # press button to submit
    # enter elements based on length and height inputs
    # calculate
    # output window show the input and output
    # go back

    # POSSIBLE CAUSES OF ERROR; wrong input data type, :window, tkinter, there is nolength and height limit. if length/height too high print invalid
    inverse_wdw.mainloop()


class Operations:
    def __init__(self):
        pass
