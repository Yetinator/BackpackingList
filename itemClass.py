import pymysql as pql

import controller
from configurations import *
from hiddenSettings import *

class Item():

    def __init__(self, id, brand, name, weightGrams):
        #U_ID	BRAND	NAME	WEIGHT_GRAMS	WHOLE_UNIT	CONTRIBUTER_ID	MODEL_YEAR	WEIGHT_OZ	PICTURE_URL	TIME_STAMP
        self.id = id
        self.brand = brand
        self.name = name
        self.weightGrams = weightGrams
        # self.wholeUnit =
        # self. contributerId =
        # self.modelYear =
        # self.weightOz =
        # self.picture_url =
        # self.timeStamp =
        self.attributes = {"Id" : self.id, "brand" : self.brand, "name" : self.name, "Weight in Grams" : self.weightGrams}

    def __str__(self):
        return self.brand + " " + self.name

    def getLongDescription(self):
        messageBoxString = ""
        for item in self.attributes:
            messageBoxString += str(item)
            messageBoxString += " : "
            messageBoxString += (str(self.attributes[item]))
            messageBoxString += ("\n")

        return messageBoxString
