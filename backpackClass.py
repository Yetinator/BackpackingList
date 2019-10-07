import pymysql as pql

import controller
from configurations import *
from hiddenSettings import *

import itemClass
import dao.BackpackDao as BackpackDao

class Backpack():

    def __init__(self, user_id, backpack_id):
        #U_ID	BRAND	NAME	WEIGHT_GRAMS	WHOLE_UNIT	CONTRIBUTER_ID	MODEL_YEAR	WEIGHT_OZ	PICTURE_URL	TIME_STAMP
        self.backpackDao = BackpackDao.BackpackDao()


        self.userId = user_id
        self.backpackId = backpack_id

        #3 lists create the temp list that exists before saving.  these should be accessed through functions and not directly
        self.itemSQLList = []
        # self.itemSQLDictionary = {}
        self.itemRemoveIdList = []
        self.itemAddList = []

        self.packWeightGrams = 0
        self.packedWeightOunces = 0
        # self.attributes = {"Id" : self.id, "brand" : self.brand, "name" : self.name, "Weight in Grams" : self.weightGrams}

    def addItemFromSQL(self, linkerId, item):
        item.linkerId = linkerId
        self.itemSQLList.append(item)
        # self.itemSQLDictionary.update({linkerId : item})

    def addUnsavedItemToTemp(self, item):
        self.itemAddList.append(item)

    def removeItemToTempUnsaved(self, viewListId):
        #this changes the list of items to be tempararily omitted from view list until saved
        #I don't know how I'm going to know the linker id on the front end yet...
        #The front end should probably not have to deal with the linkerId at all...
        list = self.getBackpackViewList()
        linkerId = list[viewListId].linkerId
        #I didn't pass linkerId forward
        #getBackpackViewList doesn't give me a linkerId either
        #some items don't have a linkerId at all.
        if (linkerId != False):
            self.itemRemoveIdList.append(linkerId)
        else:
            #remove from add list?
            #check each item in list and compare item id to item id of blah
            #it won't be the linkerId, it won't be the viewListId.. blah
            thisId = list[viewListId].id
            for i in range(len(self.itemAddList)):
                if (self.itemAddList[i].id == thisId):
                    self.itemAddList.pop(i)
                    break
            

    def getBackpackViewList(self):
        #this returns a combined list of itemSQLDictionary, itemAddList, minus itemRemoveIdList to view by front end
        #this list will be ordered here in the same order it will display in the view.
        # theItemList = []
        # #start with SQL list and subtract the removed items
        # for linkerId in self.itemSQLDictionary:
        #     if linkerId not in self.itemRemoveIdList:
        #         print(str(linkerId))
        #         theItemList.append(self.itemSQLDictionary[linkerId])
        #     else:
        #         print("not adding " + str(self.itemSQLDictionary[linkerId]))
        #
        # #add items from add list
        # for item in self.itemAddList:
        #     theItemList.append(item)
        #
        # return theItemList

        theViewItemList = []
        #start with SQL list and subtract the removed items
        for item in self.itemSQLList:
            if item.linkerId not in self.itemRemoveIdList:
                #some linkerIds will be False
                print(str(item.linkerId))
                theViewItemList.append(item)
            else:
                print("not adding " + str(item))

        #add items from add list
        for item in self.itemAddList:
            theViewItemList.append(item)

        return theViewItemList
        # return self.itemSQLList

    def saveBackpackToDatabase(self):
        #Todo I don't like the circular referacing to and from the backpackDao
        #delete items in remove list as referanced by linkerId
        for linkerId in self.itemRemoveIdList:
            self.backpackDao.removeFromBackpack(linkerId)
        #add items in itemAddList
        for item in self.itemAddList:
            userId = self.userId
            itemId = item.id
            backpackId = self.backpackId
            pocketId = 0
            self.backpackDao.insertIntoBackpack(userId, itemId, backpackId, pocketId)
        pass


    def setTotalWeights(self):
        self.packWeightGrams = 0
        list = self.getBackpackViewList()
        for item in list:
            self.packWeightGrams += item.weightGrams
        self.packedWeightOunces = round(self.packWeightGrams / 28.35, 1)




    def __str__(self):
        self.setTotalWeights()
        return "backpack quickinfo " + str(self.packWeightGrams) + " " + str(self.packedWeightOunces)

    def getLongDescription(self):
        self.setTotalWeights()
        messageBoxString = "Backpack : {}".format(self.backpackId)
        messageBoxString += ("\n")
        messageBoxString += "Grams : {}".format(self.packWeightGrams)
        messageBoxString += ("\n")
        messageBoxString += "Lbs : {} and Oz : {}".format(str(round(self.packedWeightOunces//16,0)), str(round(self.packedWeightOunces%16, 1)))
        return messageBoxString
