import tkinter as tk
import controller
from configurations import *

#pages
from HomePage import *
from PackPage import *
from NewItemPage import *




class View (tk.Tk):

    def __init__(self):

        #init the tk window part of self
        tk.Tk.__init__(self)

        #Things to change as I go
        self.pageList = (HomePage, PackPage)

        self.appController = controller.AppController()
        self.geometry(SCREEN_GEOMETRY)
        self.title(APPLICATION_NAME)

        #Functions to set up view
        self.createFileMenu()
        self.createMainFrames()
        self.createPageFrames()

    #Initializer Function
    def createFileMenu(self):
        self.menuBar = tk.Menu(self)
        self.fileMenu = tk.Menu(self.menuBar)
        self.fileMenu.add_command(label="New")
        self.fileMenu.add_command(label="Open...")
        self.fileMenu.add_command(label="View Backpack", command = self.toPackPage)
        self.fileMenu.add_command(label="Create New Item", command=self.toNewItem)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", command=self.exitProgram)
        self.menuBar.add_cascade(label="File", menu=self.fileMenu)
        self.config(menu=self.menuBar)

    #Initializer Function
    def createMainFrames(self):
        self.masterPane = tk.Frame(self, width=200, bg=CHECK_COLOR2)
        self.masterPane.pack(fill=tk.BOTH, expand=1)

    #Initialize Frames
    def createPageFrames(self):
        self.frames = {}
        for F in (self.pageList):
            frame = F(self.masterPane, self, self.appController)
            self.frames[F] = frame
            self.masterPane.grid_propagate(False)
            self.masterPane.grid_columnconfigure(0, minsize=MASTER_PANE_WIDTH)
            self.masterPane.grid_rowconfigure(0, minsize=MASTER_PANE_HEIGHT)
            frame.grid(row=0,column=0,sticky="nsew")
        # self.frames = StartPage(self.frameRandom, self)
        # self.frames = PageTwo(self.frameRandom, self)
        self.showFrame(HomePage)

    #variable Frames
    def showFrame(self, cont):
        #looking at the frames list at position cont
        for gone in self.frames:
            gone.grid_forget(self)
        frame = self.frames[cont]
        frame.tkraise()
        # frame.grid()

    #pageNavigation
    def toPackPage(self):
        self.showFrame(PackPage)

    #pageNavigation
    def toNewItem(self):
        # self.showFrame(NewItemPage)
        pass

    def exitProgram(self):
        self.quit()

app = View()

app.mainloop()
