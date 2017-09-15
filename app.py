from flask import Flask
from flask_restful import Api
from resources.albums import Albums
from resources.artists import ArtistList, Artist
from resources.songs import Songs

app = Flask(__name__)
api = Api(app)
api.secret_key='saksham'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api.add_resource(ArtistList,'/artists')
api.add_resource(Artist,'/artist/<string:name>')
api.add_resource(Albums,'/album/<string:name>')
api.add_resource(Songs,'/song/<string:name>')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port = 3000, debug=True)
