from flask import request
from flask_restful import Resource, abort, reqparse
from dijkstra import dijkstra
from flask_jwt import jwt_required

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.practiceapi

#temp db
sample_map = {
    "nodes": {
        "a": {
            "b": 1.1
        },
        "b": {
            "a": 2
        }
    }
}

maps = {
    "mapId": sample_map
}


def abort_if_map_doesnt_exist(mapId):
    if mapId not in maps:
        abort(404, message = "MapId {} doesn't exist.".format(mapId))


class Map(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'nodes', 
        required=True,
        help="The map data is invalid"
    )

    @jwt_required() ##careful! should attach ()!!
    def get(self, mapId):
        abort_if_map_doesnt_exist(mapId)
        return maps[mapId], 200
        
    
    def put(self, mapId):
        '''
        ADD validity check
        '''
        #if not valid:
        #   return 400, {"message" : "The map data is invalid."}
        data = request.get_json()
        maps[mapId] = data
        db.maps.insert_one({mapId: data})
        return maps[mapId], 200

    
class Path(Resource):
    def get(self, mapId, startId, endId):
        if mapId not in maps:
            return {"message": "Map {} is unknown.".format(mapId) }, 404 
        elif startId not in maps[mapId]['nodes']:
            return {"message": "Node {} is unknown.".format(startId)}, 404
        elif endId not in maps[mapId]['nodes']:
            return {"message": "Node {} is unknown.".format(endId)}, 404
        
        mp = maps[mapId]
        
        res = dijkstra(mp['nodes'], startId, endId)
        if "message" in res:
            print(1)
            return {"message": "There is no path between {} and {}.".format(startId, endId)}, 400
        print(2)
        return res, 200
    
        return {"message": "Something went wrong."}, 500

        
class MapList(Resource):
    def get(self):
        return maps
