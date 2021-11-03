import numpy as np
import sympy as sp
import tkinter as t
from IPython.display import display, Math
from input import *
from matrix import *


def main():
    a = Matrix(inp_length(), inp_height())
    a.enter_values()
    a.print_matrix()


if __name__ == '__main__':
    main()
