from myPackage import db

#### class model for video
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(50), nullable=False, unique=True)
    video_url = db.Column(db.String(200), nullable=False, unique=False)
    description = db.Column(db.String(500), nullable=True, unique=False)
    category = db.Column(db.String(50), nullable=True, unique=False)

    def __repr__(self):
        return self.video_name
    # one-many relationship with document table
    documents = db.relationship('Document', backref='video_name', lazy = 'dynamic')

####### class model for document
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    document_path_url = db.Column(db.String(200), nullable=False, unique=False)

