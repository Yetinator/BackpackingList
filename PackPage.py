import tkinter as tk
from configurations import *


class PackPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.config(bg="teal", relief = tk.SUNKEN, bd = 2, padx = 3, pady = 3)

        self.title = tk.Label(self, text = "PackPage", bg = TITLE_COLOR_MAIN)
        self.packedItemsFrame = tk.Frame(self, bg = CHECK_COLOR1)
        self.itemDescriptionFrame = tk.Frame(self, bg = CHECK_COLOR1)
        self.pickItemFrame = tk.Frame(self, bg=CHECK_COLOR1)

        self.title.pack()
        self.packedItemsFrame.pack(side=tk.LEFT)
        self.itemDescriptionFrame.pack(side=tk.LEFT)
        self.pickItemFrame.pack(side=tk.RIGHT)

        self.createPackedItemsFrame(self.packedItemsFrame)
        self.createItemDescriptionFrame(self.itemDescriptionFrame)
        self.createPickItemFrame(self.pickItemFrame)


    def createPackedItemsFrame(self, container):
        top = tk.Label(container, text="Packaged Items")
        self.packedBox = tk.Listbox(container)
        self.expandItemButton = tk.Button(container, text="Expand", command=self.expandItemButtonFunction)
        self.changeItemSettingsButton = tk.Button(container, text="Change", command=self.changeItemSettingsButtonFunction)

        top.pack()
        self.packedBox.pack()
        self.expandItemButton.pack()
        self.changeItemSettingsButton.pack()

    def createItemDescriptionFrame(self, container):
        top = tk.Label(container, text = "Item Description")
        messageBoxString = ""
        selectedItem = True
        attributes =  self.appController.getItemInfo(selectedItem)
        for attribute in attributes:
            messageBoxString += ("\n")
            messageBoxString += (attribute)
            messageBoxString += " : "
            messageBoxString += (attributes[attribute])
        messageBox = tk.Message(container, text=messageBoxString, width=ITEM_DESCRIPTION_WIDTH)
        top.pack()
        messageBox.pack()

    def createPickItemFrame(self, container):
        top = tk.Label(container, text = "Pick Item to add")

        messageBoxString = ""
        selectedItem = True
        itemList = self.appController.getItemList()
        self.itemListBox = tk.Listbox(container)
        for item in itemList:
            # messageBoxString += ("\n")
            # messageBoxString += (item)
            # messageBoxString += " : "
            # messageBoxString += (itemList[item])
            self.itemListBox.insert(tk.END, itemList[item])
        messageBox = tk.Message(container, text=messageBoxString, width=ITEM_DESCRIPTION_WIDTH)
        addItemButton = tk.Button(container, text = " << ", command=self.addItemButtonFunction)

        top.pack()
        self.itemListBox.pack()
        addItemButton.pack()

    def expandItemButtonFunction(self):
        #This shows item settings or subcategories in adjacent box
        print("Expand Item")

    def changeItemSettingsButtonFunction(self):
        #Does this belong here or in the expanded item?
        print("Change Item")

    def addItemButtonFunction(self):
        print("Add item to backpack")
