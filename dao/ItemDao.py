# import os
# import subprocess
# import time

import pymysql as pql
from configurations import *
from hiddenSettings import *
import itemClass

class ItemDao():

    def __init__(self):
        self.table = 'weightsSloppyImport'


    def findById(self, id):
        sqlQuery = "SELECT * from {table} WHERE UNIQUE_ID = {ID}".format(table=self.table, ID = id)

        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        result = cursor.fetchone()

        connect.close()
        theItem = itemClass.Item(result[0], result[1], result[2], result[3])
        return theItem

    def findAll(self):
        sqlQuery = "SELECT * from {table}".format(table=self.table)
        allItems = []
        
        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        connect.close()

        for record in results:
            theItem = itemClass.Item(record[0], record[1], record[2], record[3])
            allItems.append(theItem)

        return allItems
