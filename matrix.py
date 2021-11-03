from input import *
import numpy as np
import sympy as sp
import tkinter as t
from IPython.display import display, Math


class Matrix:
    def __init__(self, length, height):
        # enter matrix size
        self.length = length
        self.height = height
        self.mtx = []

    def enter_values(self):
        for i in range(self.height):
            temp = []
            for j in range(self.length):
                temp.append(inp_element())
            self.mtx.append(temp)

    def print_matrix(self):
        #mtx = np.matrix(self.mtx)
        print(self.mtx)
        #display(Math(sp.latex(sp.Matrix(sp.sympify(self.mtx, rational=True)))))

    # matrix operations
    # def add(self):
    # def sub(self):
    # def mul(self):
    # def div(self):

