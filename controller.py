import model


class AppController():
    def __init__(self):
        self.model = model.Model()

    def getItemInfo(self, selectedItem):
        wrongList = ("This is line One", "This is line two", "doe", "rey", "me")
        wrongDictionary = {"1" : "This is line One" , "2" : "This is line two", "3" : "doe", "oops" : "rey", "5" : "me"}
        item = self.model.getItemInfo(selectedItem)
        print(item)
        return item

    def getItemAtributes(self, selectedItem):
        sqlHeaders = self.model.getItemAtributes(selectedItem)
        return sqlHeaders

    def getItemList(self):
        return self.model.getItemList()

    def getItemById(self, id):
        return self.model.getItemById(id)
