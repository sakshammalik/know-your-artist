from db import db
from models.songs import SongModel
from flask_restful import Resource,reqparse


class Songs(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('album_id',
    type = int,
    required = True,
    help = "Cannot be blank")

    def post(self,name):
        if SongModel.find_by_name(name):
            return {'message':"Already exists"}, 400
        data = Songs.parser.parse_args()
        song=SongModel(name,**data)
        SongModel.save_to_db(song)
        return song.json()
