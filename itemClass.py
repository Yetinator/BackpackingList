import pymysql as pql

import controller
from configurations import *
from hiddenSettings import *

class Item():

    def __init__(self, id, brand, name, weightGrams):
        #U_ID	BRAND	NAME	WEIGHT_GRAMS	WHOLE_UNIT	CONTRIBUTER_ID	MODEL_YEAR	WEIGHT_OZ	PICTURE_URL	TIME_STAMP
        self.id = id
        #linkerId is actually used by a backpack to associate it with the backpack.  If not an item in a backpack this should return false.
        #Keep in mind an item, although identical in sql, is reconstructed for the backpack.  The linkerId is only updated in that instance
        #of that item, not in the saved version
        self.linkerId = False
        self.brand = brand
        self.name = name
        self.weightGrams = weightGrams
        self.weightOzPart = 0
        self.weightLbsPart = 0
        self.GramsToOzDivisor = 28.35
        self.weightImperialString =""
        self.setLbsOzs()
        # self.wholeUnit =
        # self. contributerId =
        # self.modelYear =
        # self.weightOz =
        # self.picture_url =
        # self.timeStamp =
        self.attributes = {"Id" : self.id, "brand" : self.brand, "name" : self.name, "Weight in Grams" : self.weightGrams, "Lbs/Oz" : self.weightImperialString}

    def setLbsOzs(self):
        totalOz = round(self.weightGrams / self.GramsToOzDivisor, 1)
        if (totalOz != 0):
            self.weightOzPart = round(totalOz % 16, 1)
            self.weightLbsPart = round(totalOz // 16, 0)
        self.weightImperialString = str(self.weightLbsPart) + " Lbs and " + str(self.weightOzPart) + " Ozs"

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
