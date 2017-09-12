from db import db

class AlbumModel(db.Model):

    __tablename__ = "albums"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    artist_id = db.Column(db.Integer, db.ForeignKey('artists.id'))
    songs = db.relationship('SongModel', lazy='dynamic')


    def __init__(self,name,artist_id):
        self.name = name
        self.artist_id = artist_id

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name = name).first()

    def json(self):
        return {'name':self.name,'songs':[song.json() for song in self.songs.all()]}


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
