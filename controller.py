import model


class AppController():
    def __init__(self):
        self.model = model.Model()

    def getItemInfo(self, selectedItem):
        wrongList = ("This is line One", "This is line two", "doe", "rey", "me")
        wrongDictionary = {"1" : "This is line One" , "2" : "This is line two", "3" : "doe", "oops" : "rey", "5" : "me"}

        return wrongDictionary

    def getItemList(self):
        wrongList = ("This is line One", "This is line two", "doe", "rey", "me")
        wrongDictionary = {"1" : "This is line One" , "2" : "This is line two", "3" : "doe", "oops" : "rey", "5" : "me"}
        return self.model.getItemList()
