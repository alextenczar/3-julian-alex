from tkinter import filedialog
from tkinter import *


def importFile():

    root = Tk()
    root.filename =  filedialog.askopenfilename()
    print (root.filename)