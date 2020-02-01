from flask import Flask, redirect, render_template, request

import controller
from webSettings import WebSettings


app = Flask(__name__)
appController = controller.AppController()
#Todo - put any variables up here I may want to maintain access to throughout the user experiance
userId = 0
backpackId = 0
pocketId = 0
webSettings = WebSettings()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/settingspage")
def settingsPage():
    return render_template("settingsPage.html")

@app.route("/fun")
def fun():
    itemlist = appController.getItemList()
    print("Fun!")
    item = appController.getItemById(1)
    # item.setSubItemList()
    # print(item)
    # for i in item.subItemList:
    #     print(i)
    return render_template("fun.html", itemlist = itemlist, formAction="/additems")

@app.route("/newitem", methods=["GET"])
def newItem():
    #Displays the page to create a new item

    #Decide whether or not we are creating a sub item and how to handle it if we are
    # pagesettings.subitem

    #si is for subitem as in the subitem radio button was selected
    isThisASubitem = request.args.get("isThisASubitem")
    parentId = request.args.get("parentId")
    subitem = False;
    if (isThisASubitem == "True"):
        subitem = True;

    parentItem = False;
    if parentId:
        parentItem = appController.getItemById(int(parentId))


    return render_template("newItem.html", isThisASubitem = subitem, parentItem = parentItem)

@app.route("/editbackpack", methods=["GET"])
def editbackpack():
    #Displays the page that shows what is in the backpack

    # itemlist = appController.getItemList()
    backpack = appController.getABackpackDirect(userId, backpackId)
    backpackList = backpack.getBackpackViewList()
    backpack.refresh()
    backpackView = backpack.getLongDescription()
    print(backpackView)

    thisRoute = "/editbackpack"
    searchBarSelection = request.args.get("searchBar")
    if not searchBarSelection:
        searchBarSelection = "itemName"

    #Todo - getBackpackViewList should be moved into the plugin controller so things don't get confusing
    #getBackpackViewList is a convoluted list that maybe doesn't save things.  It seems to work because nothing happens to the backpack inbetween summoning it and viewing it but it could cause problems.
    return render_template("editbackpack.html", itemlist = backpackList, formAction="removeitems", thisRoute=thisRoute, searchBarSelection=searchBarSelection, backpack = backpack, backpackView = backpackView, webSettings = webSettings)

@app.route("/inventory")
def inventory():
    itemlist = appController.getItemList()
    return render_template("inventory.html", itemlist = itemlist, webSettings = webSettings)

@app.route("/singleitem", methods=["GET"])
def singleItem():
    id = request.args.get("id")
    item = appController.getItemById(id)
    return render_template("singleItem.html", item=item, webSettings = webSettings)

@app.route("/additems", methods=["GET"])
def additems():
    # Add items from the inventory form to the backpack and sql
    # s?item=1&item=2&item=5
    # name = request.form.get("name")
    item = request.args.getlist("item")
    print("items are :")
    for i in item:
        print(i)
        appController.insertIntoBackpack(userId, i, backpackId, pocketId)

    return redirect("/editbackpack")

@app.route("/removeitems", methods=["GET"])
def removeitems():
    # Add items from the inventory form to the backpack and sql
    # s?item=1&item=2&item=5
    # name = request.form.get("name")
    items = request.args.getlist("item")
    print("items are :")
    linkerIdList = request.args.getlist("linkerId")
    print("linkerIds are :")

    # appController.removeFromBackpack(userId, items, backpackId, pocketId)
    appController.removeFromBackpack(linkerIdList)

    return redirect("/editbackpack")

@app.route("/settingsglobal", methods=["GET"])
def settingsglobal():
    #set global settings

    measurement = request.args.get("measurement")
    print("measurement in :")
    print(measurement)
    webSettings.unitOfMeasure = measurement


    return redirect("/settingspage")

@app.route("/settingssearch", methods=["GET"])
def settingssearch():
    #set global settings
    category = request.args.get("searchCategory")
    q = request.args.get("q")
    print("q in :")
    print(q)
    print(category)
    return redirect("/settingspage")

@app.route("/newitemsubmit", methods=["GET"])
def newItemSubmit():
    #set global settings
    thisMeasurment = request.args.get("measurement")
    category = request.args.get("searchCategory")
    brand = request.args.get("brand")
    itemName = request.args.get("itemName")
    unitOfMeasure = request.args.get("measurement")
    if (unitOfMeasure == "metric"):
        weightInGrams = request.args.get("weight")
    elif (unitOfMeasure == "imperial"):
        weightInGrams = float(request.args.get("weight")) * 28.35
    else:
        weightInGrams = False
        print("Error in weight or something")
    pocketNumber = request.args.get("pocketNumber")
    #user number will = logged in user
    # q = request.args.get("q")

    #Do something with subItem
    isThisASubitem = request.args.get("isThisASubitem")
    print("waldo" + str(isThisASubitem))
    parentId = False
    if isThisASubitem == "True":
        isThisASubitem = True;
        parentId = request.args.get("parentId")
        # childId =
    else:
        isThisASubitem = False;
    newItem = appController.createNewItem(brand, itemName, weightInGrams, isThisASubitem, parentId)
    # assign child to parent
    # if parentId != 'None':
    #     appController.assignToParent(newItem.id, parentId)
    return redirect("/newitem")
