import tkinter as tk
from configurations import *


class PackPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.config(bg="teal", relief = tk.SUNKEN, bd = 2, padx = 3, pady = 3)

        self.itemDescriptionBackpack = 2
        self.itemDescriptionInventory = 3


        self.title = tk.Label(self, text = "PackPage", bg = TITLE_COLOR_MAIN)
        self.packedItemsFrame = tk.Frame(self, bg = CHECK_COLOR1)
        self.itemDescriptionFrame = tk.Frame(self, bg = CHECK_COLOR1)
        self.itemDescriptionFrameInventory = tk.Frame(self, bg = CHECK_COLOR1)
        self.pickItemFrame = tk.Frame(self, bg=CHECK_COLOR1)

        self.title.pack()
        self.packedItemsFrame.pack(side=tk.LEFT)
        self.itemDescriptionFrame.pack(side=tk.LEFT)
        self.pickItemFrame.pack(side=tk.RIGHT)
        self.itemDescriptionFrameInventory.pack(side=tk.RIGHT)

        self.createPackedItemsFrame(self.packedItemsFrame)
        self.createItemDescriptionFrame(self.itemDescriptionFrame, self.itemDescriptionBackpack)
        self.createItemDescriptionFrame(self.itemDescriptionFrameInventory, self.itemDescriptionInventory)
        self.createPickItemFrame(self.pickItemFrame)


    #Initializer
    def createPackedItemsFrame(self, container):
        top = tk.Label(container, text="Packaged Items")
        self.packedBox = tk.Listbox(container)
        self.expandItemButton = tk.Button(container, text="Expand", command=self.expandItemButtonFunction)
        self.changeItemSettingsButton = tk.Button(container, text="Change", command=self.changeItemSettingsButtonFunction)

        top.pack()
        self.packedBox.pack()
        self.expandItemButton.pack()
        self.changeItemSettingsButton.pack()

        #Initializer
    def createItemDescriptionFrame(self, container, selectedItem):
        #There are 2 frames that rely on this same function
        #This creates the item summary for the selected item
        top = tk.Label(container, text = "Item Description")
        messageBoxString = ""
        # selectedItem = True
        attributes =  self.appController.getItemInfo(selectedItem)
        attributeLabels = self.appController.getItemAtributes(selectedItem)
        for i in range(len(attributes)):
            messageBoxString += ("\n")
            messageBoxString += (str(attributeLabels[i]))
            messageBoxString += " : "
            messageBoxString += (str(attributes[i]))
        # for attribute in attributes:
        #     messageBoxString += ("\n")
        #     messageBoxString += (str(attribute))
        #     messageBoxString += " : "
        #     messageBoxString += (str(attributes[attribute]))
        messageBox = tk.Message(container, text=messageBoxString, width=ITEM_DESCRIPTION_WIDTH)
        top.pack()
        messageBox.pack()

    def createPickItemFrame(self, container):
        #This is the right listbox
        #Items in inventory to be added to pack
        top = tk.Label(container, text = "Pick Item to add")

        itemList = self.appController.getItemList()
        self.itemListBox = tk.Listbox(container)
        for item in itemList:
            self.itemListBox.insert(tk.END, itemList[item])

        # messageBox = tk.Message(container, text=messageBoxString, width=ITEM_DESCRIPTION_WIDTH)
        addItemButton = tk.Button(container, text = " << ", command=self.addItemButtonFunction)
        self.itemListBox.bind("<Double-Button-1>", self.expandItemButtonFunction)

        top.pack()
        self.itemListBox.pack()
        addItemButton.pack()

    def expandItemButtonFunction(self,input):
        #This shows item settings or subcategories in adjacent box
        self.itemDescriptionBackpack = 2
        self.itemDescriptionInventory = self.itemListBox.curselection()
        print("Expand Item")
        print(self.itemDescriptionInventory)

    def changeItemSettingsButtonFunction(self):
        #Does this belong here or in the expanded item?
        print("Change Item")

    def addItemButtonFunction(self):
        print("Add item to backpack")
