from models.artists import ArtistModel
from flask_restful import Resource

class Artist(Resource):
    

    def get(self,name):
        artist = ArtistModel.find_by_name(name)
        if artist:
            return artist.json()
        else:
            return {'message':"{} not found".format(name)}, 404


    def post(self,name):
        if ArtistModel.find_by_name(name):
            return {'message':"Already exists"}, 400
        artist = ArtistModel(name)
        artist.save_to_db()
        return artist.json()

class ArtistList(Resource):
    def get(self):
        return {'artists':[artist.json() for artist in ArtistModel.query.all()]}
