import pymysql as pql
from configurations import *
from hiddenSettings import *
import backpackClass
import dao.ItemDao as ItemDao

class BackpackDao():

    def __init__(self):
        self.table = 'weightsSloppyImport'
        self.backpackTable = 'BACKPACK_LINKER'
        self.itemDao = ItemDao.ItemDao()


    def findByUserIdAndBackpackId(self, userId, backpackId):
        pass
        #The code below is for an item/ this is for a backpack...
        sqlQuery = "SELECT * from {table} WHERE USER_ID = '{user}' AND BACKPACK_ID = '{backpack}'".format(table=self.backpackTable, user = userId, backpack = backpackId)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        connect.close()


        #Create backpack
        theBackpack = backpackClass.Backpack(userId, backpackId)

        #add items to backpack

        for result in results:
            item = self.itemDao.findById(result[2])
            theBackpack.addItem(item)


        return theBackpack


    def insertIntoBackpack(self, userId, itemId, backpackId, pocketId):
        # UNIQUE_ID, USER_ID, ITEM_ID, BACKPACK_ID, POCKET_ID

        sqlQuery = "INSERT into {} (USER_ID, ITEM_ID, BACKPACK_ID, POCKET_ID) values({},{},{},{})".format(self.backpackTable, userId, itemId, backpackId, pocketId)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        connect.commit()
        # result = cursor.fetchone()

        connect.close()

    def removeFromBackpack(self, entryId):
        sqlQuery = "DELETE from {} WHERE UNIQUE_ID = {}".format(self.backpackTable, entryId)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        connect.commit()
        # result = cursor.fetchone()

        connect.close()
