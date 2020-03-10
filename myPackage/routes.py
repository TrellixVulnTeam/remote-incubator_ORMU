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

################ Video Updation into database #######################
#curl -i -H "Content-Type: application/json" -X PUT -d '{"category":"seriuos"}' http://localhost:5000/api/v1/incubator/resources/video/update/1

@app.route('/api/v1/incubator/resources/video/update/<int:v_id>', methods=['PUT'])
def vid_update(v_id):
    db.create_all()
    upd = Video.query.filter_by(id=v_id).first()
    if not request.json:
        abort(404)
    print(type(request.json))
    upd.category = request.json[list(request.json.keys())[0]] #request.json.get("category",upd.category)
    db.session.commit()
    return "sucess"
    
@app.route('/query')
def q():
    db.create_all()
    vname = 'jgas.mp4'
    vurl = '.assests/video/jafids.mp4'
    desc = 'jiogajsd nuaensf iuiew'
    cat = 'funny'
    vid = Video(vname, vurl, desc, cat)
    db.session.add(vid)
    doc = Document(document_path_url='j/sdg/asgasd/asg/jdsa.pdf',video_name=vid)
    db.session.add(doc)
    
    db.session.commit()
    print(Document.query.all())
    return "sucess"
    # # return jsonify({'data':User.query.all()}
