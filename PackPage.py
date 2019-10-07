import tkinter as tk
from configurations import *


class PackPage(tk.Frame):

    def __init__(self, parent, tkObj, appController):
        tk.Frame.__init__(self, parent)
        self.tkObj = tkObj
        self.parent = parent
        self.appController = appController
        self.config(bg=BACKGROUND_COLOR_MAIN, relief = tk.SUNKEN, bd = 2, padx = 3, pady = 3)

        #Variables
        self.allItemList = self.appController.getItemList()
        self.backpack = self.appController.getABackpack(0)
        self.backpackItemList = []
        self.itemDescriptionBackpack = 2
        self.itemDescriptionInventory = 3


        #Make the frames
        self.title = tk.Label(self, text = "PackPage", bg = TITLE_COLOR_MAIN, height = 2, width = 16, font = ("Bold", 16))
        self.frameBaseOne = tk.Frame(self, bg = CHECK_COLOR1)
        self.frameBaseTwo = tk.Frame(self, bg = CHECK_COLOR1)
        self.frameBaseThree = tk.Frame(self, bg = CHECK_COLOR1)
        self.frameBaseFour = tk.Frame(self, bg=CHECK_COLOR1)

        #Internal frames
        self.contentFrame1 = tk.Frame(self.frameBaseOne, bg = CHECK_COLOR1)
        self.contentFrame2 = tk.Frame(self.frameBaseTwo, bg = CHECK_COLOR1)
        self.contentFrame3 = tk.Frame(self.frameBaseThree, bg = CHECK_COLOR1)

        #pack the frames
        self.title.pack()
        self.frameBaseOne.pack(side=tk.LEFT)
        self.frameBaseTwo.pack(side=tk.LEFT)
        self.frameBaseFour.pack(side=tk.RIGHT)
        self.frameBaseThree.pack(side=tk.RIGHT)

        self.contentFrame1.pack(fill=tk.BOTH, expand=1)
        self.contentFrame2.pack(fill=tk.BOTH, expand=1)
        self.contentFrame3.pack(fill=tk.BOTH, expand=1)

        #backpack side
        self.createPackedItemsFrame(self.contentFrame1)
        # self.createItemDescriptionFrame(self.frameBaseTwo, self.itemDescriptionBackpack)

        #Inventory side
        # self.createItemDescriptionFrame(self.frameBaseThree, self.itemDescriptionInventory)
        self.createInventoryFrame(self.frameBaseFour)
        self.refreshPickedItemsFrame()

    #Initializer
    def refreshPickedItemsFrame(self):
        self.contentFrame3.pack_forget()
        self.contentFrame3 = tk.Frame(self.frameBaseThree, bg = CHECK_COLOR1)
        self.contentFrame3.pack(fill=tk.BOTH, expand=1)
        self.createItemDescriptionFrame(self.contentFrame3, self.itemDescriptionInventory)

        self.contentFrame2.pack_forget()
        self.contentFrame2 = tk.Frame(self.frameBaseTwo, bg = CHECK_COLOR1)
        self.contentFrame2.pack(fill=tk.BOTH, expand=1)
        self.createBackpackDescriptionFrame(self.contentFrame2)
        self.spacer = tk.Frame(self.contentFrame2, bg = BACKGROUND_COLOR_MAIN, height = 20).pack(fill=tk.X, expand=1)
        self.createItemDescriptionFrame(self.contentFrame2, self.itemDescriptionBackpack)

        self.contentFrame1.pack_forget()
        self.contentFrame1 = tk.Frame(self.frameBaseOne, bg = CHECK_COLOR1)
        self.contentFrame1.pack(fill=tk.BOTH, expand=1)
        self.createPackedItemsFrame(self.contentFrame1)

    #Initializer
    def createPackedItemsFrame(self, container):
        top = tk.Label(container, text="Backpack", bg = TITLE_COLOR_MAIN)
        self.packedBox = tk.Listbox(container, width=LISTBOX_WIDTH, height=LISTBOX_HEIGHT, bg = EXTRA_COLOR_2)
        self.expandItemButton = tk.Button(container, text="Expand", bg = BUTTON_COLOR_MAIN)#, command=self.expandItemButtonFunction)
        self.changeItemSettingsButton = tk.Button(container, text="Change", bg = BUTTON_COLOR_MAIN, command=self.changeItemSettingsButtonFunction)
        self.removeItemBackpackButton = tk.Button(container, text=">>", bg = BUTTON_COLOR_MAIN, command=self.removeItemBackpackFunction)
        self.saveBackpackButton = tk.Button(container, text="Save Backpack", bg = BUTTON_COLOR_MAIN, command=self.saveBackpackFunction)
        list =  self.backpack.getBackpackViewList()
        for item in list:
            self.packedBox.insert(tk.END, item)

        top.pack(fill=tk.X, expand=1)
        self.packedBox.pack()
        # self.expandItemButton.pack()
        # self.changeItemSettingsButton.pack()
        self.removeItemBackpackButton.pack()
        self.saveBackpackButton.pack()

        self.packedBox.bind("<Double-Button-1>", self.expandBackpackItemButtonFunction)

        #Initializer
    def createItemDescriptionFrame(self, container, selectedItem):
        #There are 2 frames that rely on this same function
        #This creates the item summary for the selected item
        top = tk.Label(container, text = "Item Description", bg = TITLE_COLOR_MAIN)
        item = self.appController.getItemById(selectedItem)
        messageBoxString = item.getLongDescription()
        messageBox = tk.Message(container, text=messageBoxString, bg = EXTRA_COLOR_1, width=ITEM_DESCRIPTION_WIDTH)
        top.pack(fill=tk.X, expand=1)
        messageBox.pack()

    def createBackpackDescriptionFrame(self, container):
        #There are 2 frames that rely on this same function
        #This creates the item summary for the selected item
        top = tk.Label(container, text = "Backpack Summary", bg = TITLE_COLOR_MAIN)
        messageBoxString = self.backpack.getLongDescription()
        messageBox = tk.Message(container, text=messageBoxString, bg = EXTRA_COLOR_1, width=ITEM_DESCRIPTION_WIDTH)
        top.pack(fill=tk.X, expand=1)
        messageBox.pack(fill=tk.X, expand=1)


    def createInventoryFrame(self, container):
        #This is the right listbox
        #Items in inventory to be added to pack
        top = tk.Label(container, text = "Inventory", bg = TITLE_COLOR_MAIN)


        self.itemListBox = tk.Listbox(container,width=LISTBOX_WIDTH, height = LISTBOX_HEIGHT, bg = EXTRA_COLOR_2)
        for item in self.allItemList:
            self.itemListBox.insert(tk.END, item)

        # messageBox = tk.Message(container, text=messageBoxString, width=ITEM_DESCRIPTION_WIDTH)
        addItemButton = tk.Button(container, text = " << ", bg = BUTTON_COLOR_MAIN, command=self.addItemButtonFunction)
        self.itemListBox.bind("<Double-Button-1>", self.expandItemButtonFunction)

        top.pack(fill=tk.X, expand=1)
        self.itemListBox.pack()
        addItemButton.pack()

    def expandItemButtonFunction(self, widget):
        #This shows item settings or subcategories in adjacent box
        selection = self.itemListBox.curselection()
        self.itemDescriptionInventory = self.allItemList[selection[0]].id
        self.refreshPickedItemsFrame()

    def expandBackpackItemButtonFunction(self, widget):
        selection = self.packedBox.curselection()
        #pick the item out of the backpack to expand, as an id number
        self.itemDescriptionBackpack = self.backpack.itemList[selection[0]].id
        # self.backpackItemList[selection[0]].id
        # self.allItemList[selection[0]].id
        self.refreshPickedItemsFrame()

    def removeItemBackpackFunction(self):
        selection = self.packedBox.curselection()
        print("removing item")
        print(selection[0])

        self.backpack.removeItemToTempUnsaved(selection[0])
        self.refreshPickedItemsFrame()



    def saveBackpackFunction(self):
        #There are 2 ways to save a backpack:
        # pass backpack items forward fromt the front end
        # access the backpack from the controller
        # self.appController.saveBackpack(self.backpack)
        self.backpack.saveBackpackToDatabase()

        # insertIntoBackpack(self,  userId, itemId, backpackId, pocketId)


    def changeItemSettingsButtonFunction(self):
        #Does this belong here or in the expanded item?
        print("Change Item")

    def addItemButtonFunction(self):
        #get the entry
        selection = self.itemListBox.curselection()
        uniqueId = self.allItemList[selection[0]].id
        item = self.appController.getItemById(uniqueId)
        #add to a list of items in the inventory
        # self.backpackItemList.append(item)
        self.backpack.addUnsavedItemToTemp(item)
        print("the item added will be: " + str(item))
        #have list poplulate backpack
        print("Add item to backpack")
        #refresh listbox
        self.refreshPickedItemsFrame()
        # self.packedBox.insert(tk.END, item)
