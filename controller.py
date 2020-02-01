import model
import dao.ItemDao as ItemDao
import dao.BackpackDao as BackpackDao
import itemClass

import itemClass

class AppController():
    def __init__(self):
        # self.model = model.Model()
        self.itemDao = ItemDao.ItemDao()
        self.backpackDao = BackpackDao.BackpackDao()

    def getItemList(self):
        print("Phasing out getItemList for getAllItemsList ")
        return self.itemDao.getAllItemList()

    def getAllItemsList(self):
        #better labeling of getItemList
        return self.itemDao.getAllItemList()


    def getItemById(self, id):
        return self.itemDao.findById(id)


    def getABackpack(self, index):
        # tKinter version, remove model class replace with local version of backpack - ToDo
        # return self.model.backpack[index]
        return self.backpackDao.findByUserIdAndBackpackId(0,0)

    def getABackpackDirect(self, userId, backpackId):
        #Web version skips model
        aBackpack = self.backpackDao.findByUserIdAndBackpackId(userId, backpackId)
        return aBackpack

    def saveBackpack(self, frontendBackpack):
        #this should take nothing as an input
        pass




    def insertIntoBackpack(self,  userId, itemId, backpackId, pocketId):
        self.backpackDao.insertIntoBackpack(userId, itemId, backpackId, pocketId)

    def removeFromBackpack(self,  userId, items, backpackId, pocketId):
        for i in items:
            print(i)
            #entryId must be the Linker_table unique_id...
            #but what I'm pulling from the front end is item numbers...
            #either search list and remove by item number or pass forward the linker number...
            #Todo
            backpack = self.getABackpackDirect(userId, backpackId)
            backpackList = backpack.getBackpackViewList()
            for j in backpackList:
                print(j.id)
                if int(j.id) == int(i):
                    entryId = j.linkerId
                    # appController.removeFromBackpack( entryId)
                    self.backpackDao.removeFromBackpack(entryId)

                else:
                    print("woopsie")

    def removeFromBackpack(self, linkerIdList):
        for linkerId in linkerIdList:
            print(linkerId)
            #entryId must be the Linker_table unique_id...
            #but what I'm pulling from the front end is item numbers...
            #either search list and remove by item number or pass forward the linker number...
            self.backpackDao.removeFromBackpack(linkerId)

    def createNewItem(self, brand, name, weight, subItem = False, parentId = False):
        item = itemClass.Item(brand, name, weight, subItem = subItem, parentId = parentId)
        return self.createNewItem2(item)


    def createNewItem2(self, item):
        return item.saveItem()

    def assignToParent(self, child, parent):
        self.itemDao.assignToParent(child, parent)
