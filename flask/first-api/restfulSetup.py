from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

stores = []


class Item():
    def __init__(self, name, _id, price) -> None:
        self.id = _id
        self.name = name
        self.price = price

    def convertToDict(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}


class Store():
    def __init__(self, name: str, _id: int) -> None:
        self.name = name
        self.id = _id
        self.items = []

    def addItem(self, item: Item):
        foundItems = next(filter(lambda x: x.id == item.id), None)
        if foundItems is not None:
            return {'message': 'Item already exists'}
        else:
            self.items.append(item)

    def convertToDict(self):
        # return self.items()
        res = {'name': self.name, 'id': self.id,
               'items': [item.convertToDict() for item in self.items]}
        return {'message': res}

#  fetch the store


class StoreAPI(Resource):
    def get(self, storeId):
        res = next(filter(lambda x: x.id == storeId, stores), None)
        return res.convertToDict() if res is not None else {'message': 'Not found'}
# # modify the store

    def post(self, storeId):
        try:
            body = request.get_json()
            for i in range(len(stores)):
                if stores[i].id == storeId:
                    stores[i].name = body['name']
                    return {'message': 'Done'}
            return {'message': 'failed'}
        except:
            print("Error Occured ")
# adding a new store

    def put(self, storeId):
        body = request.get_json()
        stores.append(Store(body['name'], storeId))
        return {'message': 'Done'}
# remove the store

    def delete(self, storeId):
        for i in range(len(stores)):
            if stores[i].id == storeId:
                stores.pop(i)
                return {'message': 'Done'}
        return {'message': 'failed'}


class StoreDataApi(Resource):
# * now make an Api for geting an item from a store
    def get(self, storeId, itemId):
        res = next(filter(lambda x: x.id == storeId, stores), None)
        if res is None:
            return {'message': 'Not found'}
        else:
            res1 = next(filter(lambda x: x.id == itemId, res.items), None)
            if res1 is None:
                return {'message': 'Not found'}
            else:
                return res1.convertToDict()     

# * put a new item to a store
    def put(self, storeId, itemId):
        data = request.get_json()
        res = next(filter(lambda x: x.id == storeId, stores), None)
        if res is None:
            return {'message': "Entered it store is not found"}
        else:
            itemdata = Item(data['itemname'], itemId, data['itemprice'])
            res.items.append(itemdata)
            
        return {'message': 'Done'}


# * modify price of an item in the store
    def post(self, storeId, itemId):
        data1 = request.get_json()
        for i in range(len(stores)):
            if stores[i].id == storeId:
                for item in stores[i].items:
                    if item.id == itemId:
                        var = data1.get('itemname',None)
                        var = data1.get('itemprice',None)
                        if var is not None:
                            item.name= data1['itemname']
                            item.price = data1['itemprice']
                return {'message': 'Done'}
        return {'message': 'failed'}
            
# * remove an item from the store
    def delete(self, storeId, itemId):
        for i in range(len(stores)):
            if stores[i].id == storeId:
                for j in range(len(stores[i].items)):
                    if stores[i].items[j].id == itemId:
                        stores[i].items.pop(i)
                return {'message': 'Done'}
        return {'message': 'failed'}

api.add_resource(StoreAPI, '/store/<int:storeId>')
api.add_resource(StoreDataApi, '/store/<int:storeId>/<int:itemId>')

app.run(debug=True, port=5000)
