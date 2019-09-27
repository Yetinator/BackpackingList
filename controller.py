import model


class AppController():
    def __init__(self):
        self.model = model.Model()

    def getItemList(self):
        return self.model.getItemList()

    def getItemById(self, id):
        return self.model.getItemById(id)

    def getABackpack(self, index):
        return self.model.backpack[index]
