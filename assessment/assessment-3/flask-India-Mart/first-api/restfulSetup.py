from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required, JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = 'Venkata'
api = Api(app)
CORS(app)

jwt = JWTManager(app)

stores = []
users = []


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
        res = {'name': self.name, 'id': self.id,
               'items': [item.convertToDict() for item in self.items]}
        return {'message': res}


class StoreAPI(Resource):
    def get(self, storeId):
        return {'data': [store.convertToDict() for store in stores]}, 200

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

    def put(self, storeId):
        body = request.get_json()
        stores.append(Store(body['name'], storeId))
        return {'message': 'Done'}, 201

    def delete(self, storeId):
        for i in range(len(stores)):
            if stores[i].id == storeId:
                stores.pop(i)
                return {'message': 'Done'}
        return {'message': 'failed'}


class UserAuth(Resource):
    def post(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        exists = next(filter(lambda x: x['username'] == username, users), None)
        if exists is not None:
            if exists['username'] == username and exists['password'] == password:
                token = create_access_token(
                    identity={'username': username})
                return {"data": token}, 200
            else:
                return {"message": "Invalid Password"}, 400
        else:
            return {"message": "user not found"}, 400

    def put(self):
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        exists = next(filter(lambda x: x['username'] == username, users), None)
        if exists is not None:
            return {"message": "Similar user already exists"}, 400
        users.append({"username": username, "password": password})
        return {'message': "done"}


api.add_resource(StoreAPI, '/store/<int:storeId>')
api.add_resource(UserAuth, '/user')


app.run(debug=True, port=5000)
