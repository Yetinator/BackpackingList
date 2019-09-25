import os
import subprocess
import time
# from troubleshooting import *
import pymysql as pql

import controller
from configurations import *
from hiddenSettings import *

class Model():

    def __init__(self):
        self.table = 'weightsSloppyImport'





    def getItemList(self):
        wrongDictionary = {"1" : "This is line One" , "2" : "This is line two", "3" : "doe", "oops" : "rey", "5" : "me"}
        connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        cursor = connect.cursor()

        # self.sqlQuery = "SELECT * from {table} WHERE BRAND = 'Gsi'".format(table=self.table)
        sqlQuery = "SELECT * from {table}".format(table=self.table)

        cursor.execute(sqlQuery)
        results = cursor.fetchall()

        sqlDictionary = {}
        for record in results:
            sqlDictionary[record[0]] = record[2]
            # print(record[2])

        connect.close()

        return sqlDictionary

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
