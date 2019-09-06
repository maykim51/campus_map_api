from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister
from resources.map import Map, Path, MapList



app = Flask(__name__)
api = Api(app)
app.secret_key = 'may'
jwt = JWT(app, authenticate, identity)


@app.route('/')
def home():
    return "Hi this is api homepage."

api.add_resource(Map, '/maps/<string:mapId>')
api.add_resource(Path, '/maps/<string:mapId>/path/<string:startId>/<string:endId>')
api.add_resource(MapList, '/maps')
api.add_resource(UserRegister, '/register')
app.run(port=5000, debug=True)
