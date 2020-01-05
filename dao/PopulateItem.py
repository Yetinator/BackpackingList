# import BackpackDao
# import itemDao
# import itemClass
# import backpackClass
# import raw_resourses.backpack_linker_table.csv
import os
import subprocess
import csv
import pymysql as pql
from configurations import *
from hiddenSettings import *


def populateCoolSwag():
    #move data from csv to sql table COOL_SWAG
    print("hello")
    inputs = "(U_ID, BRAND, NAME, WEIGHT_GRAMS, WHOLE_UNIT, CONTRIBUTER_ID, MODEL_YEAR, WEIGHT_OZ, PICTURE_URL, TIME_STAMP)"
    values = "('0', 'Kelty', 'Trekker 6500', '2400', '1', '0', '1234567', '84.7', 'Default.jpg', )"
    sql = "insert into COOL_SWAG {inputs}  VALUES {values};".format(inputs=inputs, values=values)

    connect = pql.connect(SQL_HOST, SQL_USER, SQL_PASSWORD, SQL_DATABASE)
    cursor = connect.cursor()

    cursor.execute(sqlQuery)
    # result = cursor.fetchone()

    connect.close()



populateCoolSwag()
