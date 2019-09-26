import os
import subprocess
import time
# from troubleshooting import *
import pymysql as pql

import controller
import itemClass
from configurations import *
from hiddenSettings import *

class Model():

    def __init__(self):
        self.table = 'weightsSloppyImport'
        self.allItems = []
        self.setItemList()



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
        # connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        # cursor = connect.cursor()
        #
        # # self.sqlQuery = "SELECT * from {table} WHERE BRAND = 'Gsi'".format(table=self.table)
        # sqlQuery = "SELECT * from {table}".format(table=self.table)
        #
        # cursor.execute(sqlQuery)
        # results = cursor.fetchall()
        #
        # sqlDictionary = {}
        # for record in results:
        #     sqlDictionary[record[0]] = record[2]
        #     # print(record[2])
        #
        # connect.close()
        #
        # return sqlDictionary

    def getItemInfo(self, item):
        sqlQuery = "SELECT * from {table} WHERE UNIQUE_ID = '{item}'".format(table=self.table, item=item)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        data = cursor.fetchone()

        connect.close()
        return data

    def getItemAtributes(self, item):
        data = ("Id", "Brand", "Item", "Weight in grams", "Notes")
        # sqlQuery = "SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = N'weightsSloppyImport'".format(table=self.table, item=item)
        #
        # connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        # cursor = connect.cursor()
        #
        # cursor.execute(sqlQuery)
        # data = cursor.fetchone()
        #
        # connect.close()
        # print(data)
        return data
