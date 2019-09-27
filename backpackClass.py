import pymysql as pql

import controller
from configurations import *
from hiddenSettings import *

import itemClass

class Backpack():

    def __init__(self, user_id, backpack_id):
        #U_ID	BRAND	NAME	WEIGHT_GRAMS	WHOLE_UNIT	CONTRIBUTER_ID	MODEL_YEAR	WEIGHT_OZ	PICTURE_URL	TIME_STAMP
        self.userId = user_id
        self.backpackId = backpack_id
        self.itemList = []
        self.packWeightGrams = 0
        self.packedWeightOunces = 0
        # self.attributes = {"Id" : self.id, "brand" : self.brand, "name" : self.name, "Weight in Grams" : self.weightGrams}
    def addItem(self, item):
        print("adding the item: " + str(item))
        self.itemList.append(item)

    def setTotalWeights(self):
        self.packWeightGrams = 0
        for item in self.itemList:
            self.packWeightGrams += item.weightGrams
        self.packedWeightOunces = round(self.packWeightGrams / 28.35, 1)




    def __str__(self):
        return self.brand + " " + self.name

    def getLongDescription(self):
        self.setTotalWeights()
        messageBoxString = "Backpack : {}".format(self.backpackId)
        messageBoxString += ("\n")
        messageBoxString += "Grams : {}".format(self.packWeightGrams)
        messageBoxString += ("\n")
        messageBoxString += "Lbs : {} and Oz : {}".format(str(round(self.packedWeightOunces//16,0)), str(round(self.packedWeightOunces%16, 1)))
        return messageBoxString
