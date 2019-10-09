import model
import dao.ItemDao as ItemDao
import dao.BackpackDao as BackpackDao

class AppController():
    def __init__(self):
        self.model = model.Model()
        self.itemDao = ItemDao.ItemDao()
        self.backpackDao = BackpackDao.BackpackDao()

    def getItemList(self):
        return self.itemDao.findAll()
        # return self.model.getItemList()

    def getItemById(self, id):
        return self.itemDao.findById(id)
        # return self.model.getItemById(id)

    def getABackpack(self, index):
        return self.model.backpack[index]

    def saveBackpack(self, frontendBackpack):
        #this should take nothing as an input
        pass
        # self.model.saveBackpack(0)



    def insertIntoBackpack(self,  userId, itemId, backpackId, pocketId):
        self.backpackDao.insertIntoBackpack(userId, itemId, backpackId, pocketId)
