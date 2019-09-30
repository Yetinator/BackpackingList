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
        self.allItems = self.itemDao.findAll()
        return 0

    #Initializer
    def setBackpackList(self):
        aBackpack = self.backpackDao.findByUserIdAndBackpackId(0,0)
        self.backpack.append(aBackpack)
        return 0

    def getItemList(self):
        return self.allItems
