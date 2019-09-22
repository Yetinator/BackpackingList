import tkinter as tk
from configurations import *


class HomePage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.config(bg="teal", relief = tk.SUNKEN, bd = 2, padx = 3, pady = 3)

        self.title = tk.Label(self, text = "HomePage", bg = TITLE_COLOR_MAIN)
        self.title.pack()
