from flask import Flask, redirect, render_template, request

import controller

app = Flask(__name__)
appController = controller.AppController()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fun")
def fun():
    return render_template("fun.html")

@app.route("/editbackpack")
def editbackpack():
    # itemlist = appController.getItemList()
    backpack = appController.getABackpack(0)
    backpackList = backpack.getBackpackViewList()
    #Todo - getBackpackViewList should be moved into the plugin controller so things don't get confusing
    return render_template("editbackpack.html", itemlist = backpackList)

@app.route("/inventory")
def inventory():
    itemlist = appController.getItemList()
    return render_template("inventory.html", itemlist = itemlist)

@app.route("/additems", methods=["GET"])
def additems():
    # Add items from the inventory form to the backpack and sql
    # s?item=1&item=2&item=5
    # name = request.form.get("name")
    item = request.args.getlist("item")
    print("items are :")
    for i in item:
        print(i)

    return redirect("/editbackpack")
