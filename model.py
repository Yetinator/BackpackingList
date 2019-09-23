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
        self.connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
        self.cursor = self.connect.cursor()

        # self.sqlQuery = "SELECT * from {table} WHERE BRAND = 'Gsi'".format(table=self.table)
        self.sqlQuery = "SELECT * from {table}".format(table=self.table)

        self.cursor.execute(self.sqlQuery)
        self.results = self.cursor.fetchall()

        sqlDictionary = {}
        for record in self.results:
            sqlDictionary[record[0]] = record[2]
            # print(record[2])

        self.connect.close()

        return sqlDictionary
