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

class Model():

    def __init__(self):
        self.table = 'weightsSloppyImport'
        self.allItems = []
        self.backpackDao = BackpackDao.BackpackDao()
        #there is actually only one backpack unless the implementation gets weird
        self.backpack = []
        self.setItemList()
        self.setBackpackList()


    #Initializer
    def setItemList(self):
        sqlQuery = "SELECT * from {table}".format(table=self.table)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        connect.close()

        for record in results:
            theItem = itemClass.Item(record[0], record[1], record[2], record[3])
            self.allItems.append(theItem)

        return 0

    #Initializer
    def setBackpackList(self):
        #later will call from sql and import appropriate backpacks or something
        #userid, backpackid
        # aBackpack = backpackClass.Backpack(1,1)
        aBackpack = self.backpackDao.findByUserIdAndBackpackId(0,0)
        self.backpack.append(aBackpack)

    def getItemById(self, id):
        sqlQuery = "SELECT * from {table} WHERE UNIQUE_ID = {ID}".format(table=self.table, ID = id)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        result = cursor.fetchone()

        connect.close()
        theItem = itemClass.Item(result[0], result[1], result[2], result[3])
        return theItem

    def getItemList(self):
        return self.allItems


    # def getItemInfo(self, item):
    #     sqlQuery = "SELECT * from {table} WHERE UNIQUE_ID = '{item}'".format(table=self.table, item=item)
    #
    #     connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
    #     cursor = connect.cursor()
    #
    #     cursor.execute(sqlQuery)
    #     data = cursor.fetchone()
    #
    #     connect.close()
    #     return data
