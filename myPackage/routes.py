from flask import jsonify, request, abort, make_response
from myPackage.models.user import User, Login
from myPackage.models.gallery import Video, Document
from myPackage import app, db


@app.route('/')
@app.route('/home')
def home():
    return "<h1>REMOTE INCUBATOR</h1>"

########## user registration
@app.route('/api/v1/incubator/resources/user/registration/create',methods=['POST'])
def regis():
    values =[]
    if not request.json:
        abort(404)
    for i in request.json:
        values.append(request.json[i])

    db.create_all()
    new_user = User(name=values[0],password=values[1],contact=values[2],email=values[3],company=values[4],design=values[5],why=values[6],address=values[7])
    log = Login(id=new_user.user_id, login_id=new_user.email, password=new_user.password)

    db.session.add(new_user)
    db.session.add(log)
    db.session.commit()
    
    return "value inserted in user and login tables"

############ Video Insertion into database #######################
@app.route('/api/v1/incubator/resources/video/create', methods=['POST'])
def videoDoc():
    values = []
    if not request.json:
        abort(404)
    for i in request.json:
        values.append(request.json[i])
    
    db.create_all()
    vid = Video(video_name=values[0], video_url=values[1], description=values[2], category=values[3])
    db.session.add(vid)
    # adding documents to video
    doc = Document(document_path_url="./assests/etc.pdf")
    db.session.add(doc)
    db.session.commit()
    return "Inserted into Video table and document table"
    
@app.route('/query')
def q():
    db.create_all()
    print(User.query.all())
    return "sucess"
    # # return jsonify({'data':User.query.all()}
