import os
import subprocess
import time
# from troubleshooting import *
import pymysql as pql

import controller
import itemClass
import backpackClass
from configurations import *
from hiddenSettings import *
import dao.BackpackDao as BackpackDao
import dao.ItemDao as ItemDao

class Model():
    #I don't recall why this model class exists.  I think I was trying to remove data referances from the front end in tkinter
    #I'm not sure this has any application in web
    #This does allow comparisons in tkinter later so I know what needs to be added.  tkinter is stupid or I can't use it.
    #Todo - phase out model and use local backpack as a local copy for comparision with sql

    def __init__(self):
        # self.table = 'weightsSloppyImport'
        self.backpackDao = BackpackDao.BackpackDao()
        self.itemDao = ItemDao.ItemDao()

        #list of sql items
        self.allItems = []
        #there is actually only one backpack unless the implementation gets weird
        self.backpack = []


        self.setItemList()
        self.setBackpackList()


    #Initializer
    def setItemList(self):
        print("Doing something in Model class.  Remove Model class.  ")
        #this is setting the non-backpack total list of everything for the front end.
        self.allItems = self.itemDao.findAll()
        return 0

    #Initializer
    def setBackpackList(self):
        print("Doing something in Model class.  Remove Model class.  ")
        #create a backpack in the model for use elswhere
        aBackpack = self.backpackDao.findByUserIdAndBackpackId(0,0)
        self.backpack.append(aBackpack)
        return 0

    def getItemList(self):
        print("Doing something in Model class.  Remove Model class.  ")
        # print("possibly obsolete function getItemList in Model class")
        return self.backpack.getBackpackViewList()

    def saveBackpack(self, iValue):
        #compare dao backpack to local
        print("possibly obsolete function saveBackpack in Model class this function does literally nothing")
        print("Doing something in Model class.  Remove Model class.  ")
        pass
        # localBackpack = self.backpack[iValue]
        # sqlBackpack = self.backpackDao.findByUserIdAndBackpackId(localBackpack.userId, localBackpack.backpackId)
        #
        # addItemIds = []
        # removeBackpackIds = []
        # #pick items to add
        # #juggle list id, item id, backpack connection id.. bah!
        # for index in range(len(localBackpack.itemList)):
        #
        #     if (linkerId not in sqlBackpack.itemList):
        #         print("this is j " + str(j))


        #make the changes
