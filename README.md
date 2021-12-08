# Matrix Calculator
A desktop application that returns the inverse, product, sum, and transpose of matrices with dimensions up to 4x4. Written in Python using Tkinter and Numpy.

## How to install and run
1. Install Python 3.6+ from the official website.
2. Install the dependencies: Sumpy, Tkinter, and Matplotlib by running `pip/pip3 install <dependency_name>` from the terminal.
3. Download/clone the repository then unzip the files.
4. Find the folder containing main.py.
5. Run from the terminal `python/python3 main.py` or use your IDE.

## Features
* Utilizes Numpy for matrix operations.
* Inverse, transpose, multiply, and add are supported operations.
* Matrix dimensions up to 4x4 are supported.

## Known issues:
* Computed matrices become 1D lists of strings (may be solved by converting a space seperated string to elements in list)
* Output elements are not seperated by columns
* New windows spawn randomly outside Mutter window manager; such as windows10 (may be solved by 
                                                                switching to frame-by-frame control)
* Running this on Windows10 is not the best user experience.

## Possible updates:
* Code refactoring for readability and reusability.
* Change to frame by frame control system instead of destroying windows.


### MENU
![menu](https://i.ibb.co/ThDw5wG/1.png)
### INVERSE
![inverse](https://i.ibb.co/85B9LLv/2.png)
![inverse input](https://i.ibb.co/DRywQQt/3.png)
![inverse output](https://i.ibb.co/ySRQxM8/4.png)
### MULTIPLY
![multiply](https://i.ibb.co/ZHr5Cf9/5.png)
![multiply input](https://i.ibb.co/zQbXP4c/6.png)
![multiply output](https://i.ibb.co/0XgwJBs/7.png)
<!--* ![multiply2 input](https://i.ibb.co/XW6gLNw/8.png)
* ![multiply2_output](https://i.ibb.co/XyvzbR7/9.png) -->
### ADD
![add input](https://i.ibb.co/GvW9rM5/10.png)
![add_output](https://i.ibb.co/0KL4NYc/11.png)
### TRANSPOSE
![transpose input](https://i.ibb.co/v4x1tF0/12.png)
![transpose output](https://i.ibb.co/fD40jfn/13.png)


