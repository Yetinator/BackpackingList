# import os
# import subprocess
# import time

import pymysql as pql
from configurations import *
from hiddenSettings import *
import itemClass

class ItemDao():

    # Itemtable = 'weightsSloppyImport'
    Itemtable = 'item'

    def __init__(self):
        # self.table = 'weightsSloppyImport'
        self.table = 'item'
        self.parentTable = 'parent_child'


    def findById(self, id):
        # sqlQuery = "SELECT * from {table} WHERE UNIQUE_ID = {ID}".format(table=self.table, ID = id)
        sqlQuery = "SELECT * from {table} WHERE item_id = {ID}".format(table=self.table, ID = id)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE, cursorclass=pql.cursors.DictCursor)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        result = cursor.fetchone()

        connect.close()
        theItem = itemClass.Item(result["item_brand"], result["item_name"], result["item_weight_grams"], result["item_id"])
        return theItem

    def findAll(self):
        #Todo rename getAllItemList()
        #copy of this function created below - phase this labeling out

        sqlQuery = "SELECT * from {table}".format(table=self.table)
        allItems = []

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE, cursorclass=pql.cursors.DictCursor)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        connect.close()

        for result in results:
            theItem = itemClass.Item(result["item_brand"], result["item_name"], result["item_weight_grams"], result["item_id"])
            allItems.append(theItem)

        return allItems



    def getAllItemList(self):
        #This is a replacement for findAll

        sqlQuery = "SELECT * from {table} WHERE nolist_not_full_part != 1".format(table=self.table)
        allItems = []

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE, cursorclass=pql.cursors.DictCursor)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        connect.close()

        for result in results:
            theItem = itemClass.Item(result["item_brand"], result["item_name"], result["item_weight_grams"], result["item_id"])
            allItems.append(theItem)

        return allItems

    def createNewEntry(self, brand, itemName, itemWeightInGrams, UID, isSubItem):
        # sqlQuery = "INSERT into {table} (UNIQUE_ID, BRAND, ITEM_NAME, ITEM_WEIGHT, NOTES) VALUES ({UID}, '{brand}', '{itemName}', {itemWeight}, '{notes}')".format(table=self.table, UID = int(UID), brand= brand, itemName=itemName, itemWeight=int(itemWeightInGrams), notes = "None")
        # INSERT INTO weightsSloppyImport (UNIQUE_ID, BRAND, ITEM_NAME, ITEM_WEIGHT, NOTES) VALUES (300, 'testBrand', 'test Name', 435, 'NONE');

        isSubInt = 0
        if isSubItem == True:
            isSubInt = 1

        sqlQuery = "INSERT into {table} (item_brand, item_name, item_weight_grams, item_notes, nolist_not_full_part) VALUES ('{brand}', '{itemName}', {itemWeight}, '{notes}', '{isSubItem}')".format(table=self.table, UID = int(UID), brand= brand, itemName=itemName, itemWeight=int(itemWeightInGrams), notes = "None", isSubItem=isSubInt)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        connect.commit()

        connect.close()

    def nextUid(self):
        # sqlQuery = "SELECT MAX(UNIQUE_ID) from {table}".format(table=self.table)
        sqlQuery = "SELECT MAX(item_id) from {table}".format(table=self.table)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        result = cursor.fetchone()
        # result = int(result) + 1

        result = int(result[0]) + 1



        connect.close()
        return result

    def assignToParent(self, childId, parentId):
        if parentId == 'None':
            return "Failure"

        sqlQuery = "INSERT into {parentTable} (parent_item_id, child_item_id) VALUES ('{parentId}', '{childId}')".format(parentTable=self.parentTable, parentId=parentId, childId=childId)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        connect.commit()

        connect.close()

    def getSubItems(self, id):
        #for an item, return a list of subitems

        sqlQuery = """SELECT
                    i.item_id,
                    i.item_name,
                    i.item_brand,
                    i.item_weight_grams,
                    i.item_notes

                    FROM {parentTable} p
                    JOIN {itemTable} i
                    ON p.child_item_id = i.item_id
                    WHERE p.parent_item_id = {parentId};""".format(parentTable=self.parentTable, itemTable=self.table, parentId = id)
        allItems = []

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE, cursorclass=pql.cursors.DictCursor)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        connect.close()

        for result in results:
            theItem = itemClass.Item(result["item_brand"], result["item_name"], result["item_weight_grams"], result["item_id"])
            allItems.append(theItem)

        return allItems
