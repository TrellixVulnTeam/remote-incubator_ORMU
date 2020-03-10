from myPackage import db

#### class model for video
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_name = db.Column(db.String(50), nullable=False, unique=True)
    video_url = db.Column(db.String(200), nullable=False, unique=False)
    description = db.Column(db.String(500), nullable=True, unique=False)
    category = db.Column(db.String(50), nullable=True, unique=False)
    
    def __init__(self,video_name,video_url, description, category):
        
        self.video_name = video_name
        self.video_url = video_url
        self.description = description
        self.category = category

    def __repr__(self):
        return self.video_name
        # jdata = {'id':id, 'video_name':self.video_name,'video_url':self.video_url,'description':self.description,'category':self.category}
    # one-many relationship with document table
    documents = db.relationship('Document', backref='video_name', lazy = True)

####### class model for document
class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'))
    document_path_url = db.Column(db.String(200), nullable=False, unique=False)

    def __repr__(self):
        return str(self.video_id)