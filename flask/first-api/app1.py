
from flask import Flask, request, jsonify
app = Flask(__name__)

# @app.route("/world", methods=["POST"])
# def home():
#     print(request.get_json())
#     return "Hello World"


@app.route("/hello")
def homeNew():
    return "Hello Venkata"


@app.route("/how")
def homeNewdesign():
    reqObj = request.get_json()
    print(f"Name is {reqObj['name']} and Id is {reqObj['id']}")
    reqObj["id"] = 10
    return jsonify(reqObj)


@app.route("/hi")
def homeNewthing():
    return "Hello!, Hi, How are you?"

# *


@app.route("/", methods=["POST"])
def initiate():
    reqObj = request.get_json()
    print(f"Stores = Name {reqObj['name']}, Items {reqObj['items']}")
    return jsonify(reqObj)


@app.route("/h", methods=["POST"])
def initiateNew():
    reqObj = request.get_json()
    print(f"Items = {reqObj['items']}")
    return jsonify(reqObj)


@app.route("/ho", methods=["POST"])
def initiateNewthing():
    reqObj = request.get_json()
    print(f"Name {reqObj['name']}")
    return jsonify(reqObj)


# stores = [{"name": "Raman Store", "items": [
#     {"name": "shirt", "qty": 56}, {"name": "pant", "qty": 34}]}]


# @app.route("/add/store")
# def getStores():
#     newStore = request.get_json()
#     stores.append(newStore)
#     return jsonify({"data": stores})


# @app.route("/add/item")
# def getAllStores():
#     reqObj = request.get_json()
#     for i in range(len(stores)):
#         if stores[i] == reqObj["storeId"]:
#             stores[i]["items"].append(reqObj)


# @app.route("/store/<int:storeId>/item/<int:itemId>qty", methods=["POST"])
# def changeStore(storeId, itemId):
#     requestObj = request.get_json()
#     for store in stores:
#         if store["id"] == storeId:
#             for item in store["items"]:
#                 if item["id"] == itemId:
#                     item["qty"] == requestObj['qty']
#                     print(stores)
#                 else:
#                     print("item not found")
#         else:
#             print("store not found")
#     return "task completed"


app.run(debug=True, port=5000)
