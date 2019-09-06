from flask_restful import Resource, reqparse
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.practiceapi


class User:
    parser = reqparse.RequestParser()
    parser.add_argument("username")
    parser.add_argument("password")
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


class UserList:
    users = [
        User(1, 'anne', '1234'),
        User(2, 'bob', '1234'),
        User(3, 'chris', '1234')
    ]
    
    @classmethod
    def add(cls, user):
        global db
        db.users.insert_one({'username':user.username, 'password': user.password})
        cls.users.append(user)
    
    @classmethod
    def get_userid_mapping(cls):
        return {u.id: u for u in cls.users}
        
    @classmethod
    def get_username_mapping(cls):
        return {u.username: u for u in cls.users}
    

class UserRegister(Resource):
    def post(self):
        data = User.parser.parse_args()
        user = User(len(UserList.users)+1, data['username'], data['password'])
        UserList.add(user)
        return {'user': data}, 201


