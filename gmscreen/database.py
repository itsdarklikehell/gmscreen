from flask_sqlalchemy import SQLAlchemy
from gmscreen import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gmscreen.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ViewSystem(db.Model):
    """Represents a specific group and layout of Viewports."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(120))
    viewports = db.relationship('Viewport', backref='viewsystem', lazy='dynamic')
    playlists = db.relationship('Playlist', backref='viewsystem', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'viewports': [v.to_dict() for v in self.viewports],
            'playlists': [p.to_dict() for p in self.playlists]
        }


class Viewport(db.Model):
    """Represents an individual device or screen capable of playing back media."""
    id = db.Column(db.Integer, primary_key=True)
    viewsystem_id = db.Column(db.Integer, db.ForeignKey('viewsystem.id'), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    code = db.Column(db.String(30), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'viewsystem_id': self.viewsystem_id
        }


class Playlist(db.Model):
    """Represents a playlist to be replayed on a particular ViewSystem."""
    id = db.Column(db.Integer, primary_key=True)
    viewsystem_id = db.Column(db.Integer, db.ForeignKey('viewsystem.id'), nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'viewsystem_id': self.viewsystem_id
        }


class PlayState(db.Model):
    """Represents a single combined state of components on a viewport."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    background_uri = db.Column(db.String(300))
    music_uri = db.Column(db.String(300))
    video_uri = db.Column(db.String(300))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'background_uri': self.background_uri,
            'music_uri': self.music_uri,
            'video_uri': self.video_uri
        }


with app.app_context():
    db.create_all()
