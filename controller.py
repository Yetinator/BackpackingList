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
        #compare current backpack to database
        #if item is in database already do nothing
        #if item is not in database already insert item
        #if item is in database, but not current list remove item
        inDatabase = self.backpackDao.findByUserIdAndBackpackId(0,0).itemList
        inCurrentList = frontendBackpack.itemList
        inDatabaseIds = []
        inCurrentListIds = []
        userId = 0
        # itemId = False
        backpackId = 0
        pocketId = 0

        for i in inDatabase:
            print("In inDatabase item: " + str(i.id))
            inDatabaseIds.append(i.id)
        for y in inCurrentList:
            inCurrentListIds.append(y.id)

        for j in range(len(inCurrentList)):
            print("Testing item: " + str(inCurrentList[j].id))
            if (inCurrentList[j].id not in inDatabaseIds):
                self.backpackDao.insertIntoBackpack(userId, inCurrentList[j].id, backpackId, pocketId)
            else:
                print("Already in database: " + str(inCurrentList[j].id))

        #delete some stuff if removed
        for x in inDatabaseIds:
            if x not in inCurrentListIds:
                print("removing item " + str(x))
                self.backpackDao.removeFromBackpack(x)


    def insertIntoBackpack(self,  userId, itemId, backpackId, pocketId):
        self.backpackDao.insertIntoBackpack(userId, itemId, backpackId, pocketId)
