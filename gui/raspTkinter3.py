import tkinter as tk

#this codebox represents a "baseline" future "StartPage" will be defined later
class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        #StartPage is a page we are about to make a class for
        for F in (StartPage, PageOne):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        #looking at the frames list at position cont
        frame = self.frames[cont]
        frame.tkraise()


#startPage class from the codebox above

LARGE_FONT = ("Verdana" ,14)

class ParentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        #LARGE_FONT defined above
        label = tk.Label(self, text = "Parent?", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
        button1.pack()

class StartPage(tk.Frame):
    pass
    # def __init__(self, parent, controller):
    #     tk.Frame.__init__(self,parent)
    #     #LARGE_FONT defined above
    #     label = tk.Label(self, text = "What the?", font=LARGE_FONT)
    #     label.pack(pady=10, padx=10)
    #
    #     button1 = tk.Button(self, text="Visit Page 1", command=lambda: controller.show_frame(PageOne))
    #     button1.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Back to home", command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = SeaofBTCapp()
app.mainloop()
