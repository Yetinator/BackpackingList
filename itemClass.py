import pymysql as pql

# import controller
import dao.ItemDao as ItemDao
from configurations import *
from hiddenSettings import *

class Item():

    def getItemList():
        #don't list self in a class called function
        #this is circular, an itemDao creates an item out of sql info and returns it.  Todo - Dump this function
        return ItemDao.ItemDao.getAllItemList()

    # def __init__(self, brand, name, weightGrams):
    #     self.itemDao = ItemDao.ItemDao()
    #     id = self.itemDao.nextUid()
    #     __init__(id, brand, name, weightGrams)




    def __init__(self, brand, name, weightGrams, id=False, subItem = False, parentId = False):
        #U_ID	BRAND	NAME	WEIGHT_GRAMS	WHOLE_UNIT	CONTRIBUTER_ID	MODEL_YEAR	WEIGHT_OZ	PICTURE_URL	TIME_STAMP
        self.itemDao = ItemDao.ItemDao()
        if(id==False):
            self.id = self.itemDao.nextUid()
            if(self.id==False):
                self.id = False
        else:
            self.id = id
        #linkerId is actually used by a backpack to associate it with the backpack.  If not an item in a backpack this should return false.
        #Keep in mind an item, although identical in sql, is reconstructed for the backpack.  The linkerId is only updated in that instance
        #of that item, not in the saved version
        self.linkerId = False
        self.brand = brand
        self.name = name
        self.weightGrams = weightGrams
        self.weightOzPart = 0
        self.weightLbsPart = 0
        self.GramsToOzDivisor = 28.35
        self.weightImperialString =""
        self.setLbsOzs()
        self.isSubItem = subItem
        self.subItemList = []
        self.parentId = parentId
        # self. contributerId =
        # self.modelYear =
        # self.weightOz =
        # self.picture_url =
        # self.timeStamp =

        #self.attributes is used to make a display string
        self.attributes = {"Id" : self.id, "brand" : self.brand, "name" : self.name, "Weight in Grams" : self.weightGrams, "Lbs/Oz" : self.weightImperialString}
        self.setSubItemList()


    def setLbsOzs(self):
        totalOz = round(float(self.weightGrams) / self.GramsToOzDivisor, 1)
        if (totalOz != 0):
            self.weightOzPart = round(totalOz % 16, 1)
            self.weightLbsPart = round(totalOz // 16, 0)
        self.weightImperialString = str(self.weightLbsPart) + " Lbs and " + str(self.weightOzPart) + " Ozs"

    def setSubItemList(self):
        self.subItemList = self.itemDao.getSubItems(self.id)




    def __str__(self):
        return self.brand + " " + self.name

    def getLongDescription(self):
        messageBoxString = ""
        for item in self.attributes:
            messageBoxString += str(item)
            messageBoxString += " : "
            messageBoxString += (str(self.attributes[item]))
            messageBoxString += ("\n")
        return messageBoxString

    def assignToParent(self):
        parentId = self.parentId
        childId = self.id
        if parentId != False and childId != False:
            self.itemDao.assignToParent(childId, parentId)

    def saveItem(self):

        self.itemDao.createNewEntry(self.brand, self.name, self.weightGrams, self.id, isSubItem=self.isSubItem)
        self.assignToParent()
        return self
