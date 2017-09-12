from db import db
class ArtistModel(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    albums = db.relationship('AlbumModel', lazy = 'dynamic')

    def __init__(self,name):
        self.name = name

    def json(self):
        return {'name':self.name,'albums':[album.json() for album in self.albums.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls,name):
        return cls.query.filter_by(name= name).first()
