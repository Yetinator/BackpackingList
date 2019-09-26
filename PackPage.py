import tkinter as tk
from configurations import *


class PackPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.config(bg="teal", relief = tk.SUNKEN, bd = 2, padx = 3, pady = 3)

        #Variables
        self.allItemList = self.appController.getItemList()
        self.itemDescriptionBackpack = 2
        self.itemDescriptionInventory = 3


        #Make the frames
        self.title = tk.Label(self, text = "PackPage", bg = TITLE_COLOR_MAIN)
        self.itemsCurrentlyInBackpackFrame = tk.Frame(self, bg = CHECK_COLOR1)
        self.itemDescriptionForBackpackSelectionFrame = tk.Frame(self, bg = CHECK_COLOR1)
        self.itemDescriptionFrameInventory = tk.Frame(self, bg = CHECK_COLOR1)
        self.itemInventoryFrame = tk.Frame(self, bg=CHECK_COLOR1)

        #pack the frames
        self.title.pack()
        self.itemsCurrentlyInBackpackFrame.pack(side=tk.LEFT)
        self.itemDescriptionForBackpackSelectionFrame.pack(side=tk.LEFT)
        self.itemInventoryFrame.pack(side=tk.RIGHT)
        self.itemDescriptionFrameInventory.pack(side=tk.RIGHT)

        #backpack side
        self.createPackedItemsFrame(self.itemsCurrentlyInBackpackFrame)
        # self.createItemDescriptionFrame(self.itemDescriptionForBackpackSelectionFrame, self.itemDescriptionBackpack)

        #Inventory side
        self.createItemDescriptionFrame(self.itemDescriptionFrameInventory, self.itemDescriptionInventory)
        self.createPickItemFrame(self.itemInventoryFrame)


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
        item = self.appController.getItemById(selectedItem)
        messageBoxString = item.getLongDescription()
        messageBox = tk.Message(container, text=messageBoxString, width=ITEM_DESCRIPTION_WIDTH)
        top.pack()
        messageBox.pack()


    def createPickItemFrame(self, container):
        #This is the right listbox
        #Items in inventory to be added to pack
        top = tk.Label(container, text = "Pick Item to add")


        self.itemListBox = tk.Listbox(container)
        for item in self.allItemList:
            # self.itemListBox.insert(tk.END, itemList[item])
            # self.itemListBox.insert(tk.END, item.name)
            print("this is item: " + str(item.name))
            print("this is id: " + str(item.id))
            self.itemListBox.insert(tk.END, item)

        # messageBox = tk.Message(container, text=messageBoxString, width=ITEM_DESCRIPTION_WIDTH)
        addItemButton = tk.Button(container, text = " << ", command=self.addItemButtonFunction)
        self.itemListBox.bind("<Double-Button-1>", self.expandItemButtonFunction)

        top.pack()
        self.itemListBox.pack()
        addItemButton.pack()

    def expandItemButtonFunction(self,input):
        #This shows item settings or subcategories in adjacent box
        selection = self.itemListBox.curselection()
        print("this is selection: " + str(selection) + "Of type: " + str(type(selection)))
        print("allItemList comparison: " + str(self.allItemList[selection[0]]) + " " + str(self.allItemList[selection[0]].brand))
        self.itemDescriptionBackpack = 2
        self.itemDescriptionInventory = self.allItemList[selection[0]].id
        print("Expand Item")
        self.createItemDescriptionFrame(self.itemDescriptionFrameInventory, self.itemDescriptionInventory)
        print(str(self.itemDescriptionInventory))

    def changeItemSettingsButtonFunction(self):
        #Does this belong here or in the expanded item?
        print("Change Item")

    def addItemButtonFunction(self):
        print("Add item to backpack")
