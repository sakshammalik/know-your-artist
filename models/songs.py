from db import db

class SongModel(db.Model):

    __tablename__ = "songs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    album_id = db.Column(db.Integer, db.ForeignKey('albums.id'))

    def __init__(self,name,album_id):
        self.name = name
        self.album_id = album_id

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name = name).first()

    def json(self):
        return {'name':self.name}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
