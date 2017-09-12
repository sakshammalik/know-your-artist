from db import db
from models.albums import AlbumModel
from flask_restful import Resource,reqparse

class Albums(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('artist_id',
    type = int,
    required = True,
    help = "Cannot be blank")

    def get(self,name):
        album = Album.find_by_name(name)
        if album:
            return album.json()
        else:
            return {'message':"{} not found.".format(name)}, 404

    def post(self,name):
        if AlbumModel.find_by_name(name):
            return {'message':"Already exists"}, 400
        data = Albums.parser.parse_args()
        album=AlbumModel(name,**data)
        AlbumModel.save_to_db(album)
        return album.json()

    def delete(self,name):
        if AlbumModel.find_by_name(name):
            data = Albums.parser.parse_args()
            album = AlbumModel(name,**data)
            AlbumModel.delete_from_db(album)
            return {'message':"{} album deleted".format(name)}
        return {'message':"Album deleted."}
