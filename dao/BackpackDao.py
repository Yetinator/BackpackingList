import pymysql as pql
from configurations import *
from hiddenSettings import *
import backpackClass
import dao.ItemDao as ItemDao

class BackpackDao():
    #The BackpackDao is for communicating with sql
# findByUserIdAndBackpackId
# insertIntoBackpack(self, userId, itemId, backpackId, pocketId)
# removeFromBackpack(self, entryId):
    #make sure entryId is the UNIQUE_ID of the backpack entry row not of the item


    def __init__(self):
        # self.table = 'weightsSloppyImport'
        # self.backpackTable = 'BACKPACK_LINKER'
        self.table = 'item'
        self.backpackTable = 'backpack'
        self.itemDao = ItemDao.ItemDao()


    def findByUserIdAndBackpackId(self, userId, backpackId):
        # pass
        #The code below is for an item/ this is for a backpack...
        # sqlQuery = "SELECT * from {table} WHERE USER_ID = '{user}' AND BACKPACK_ID = '{backpack}'".format(table=self.backpackTable, user = userId, backpack = backpackId)
        sqlQuery = "SELECT * from {table} WHERE user_id = '{user}' AND backpack_id = '{backpack}'".format(table=self.backpackTable, user = userId, backpack = backpackId)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE, cursorclass=pql.cursors.DictCursor)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        connect.close()


        #Create backpack
        theBackpack = backpackClass.Backpack(userId, backpackId)

        #add items to backpack
        for result in results:
            # linkerId = result[0]
            # print("waldo")
            # print(result['u_id'])
            # item = self.itemDao.findById(result[1])
            # theBackpack.addItemFromSQL(linkerId, item)

            linkerId = result['u_id']
            item = self.itemDao.findById(result['item_id'])
            theBackpack.addItemFromSQL(linkerId, item)



        return theBackpack


    def insertIntoBackpack(self, userId, itemId, backpackId, pocketId):
        # UNIQUE_ID, USER_ID, ITEM_ID, BACKPACK_ID, POCKET_ID

        # sqlQuery = "INSERT into {} (USER_ID, ITEM_ID, BACKPACK_ID, POCKET_ID) values({},{},{},{})".format(self.backpackTable, userId, itemId, backpackId, pocketId)
        sqlQuery = "INSERT into {} (user_id, item_id, backpack_id, pocket_id) values({},{},{},{})".format(self.backpackTable, userId, itemId, backpackId, pocketId)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        connect.commit()
        # result = cursor.fetchone()

        connect.close()

    def removeFromBackpack(self, linkerId):
        #make sure entryId is the UNIQUE_ID of the backpack entry row not of the item
        # sqlQuery = "DELETE from {} WHERE UNIQUE_ID = {}".format(self.backpackTable, linkerId)
        sqlQuery = "DELETE from {} WHERE u_id = {}".format(self.backpackTable, linkerId)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        connect.commit()
        # result = cursor.fetchone()

        connect.close()
