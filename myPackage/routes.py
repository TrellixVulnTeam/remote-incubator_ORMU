from flask import jsonify, request, abort, make_response
from myPackage.models.user import User, Login
from myPackage.models.gallery import Video, Document
from myPackage import app, db

##################### home ##########################################################################
@app.route('/')
@app.route('/home')
def home():
    return "<h1>REMOTE INCUBATOR</h1>"
###################################################################################################

########################## user REGISTRATION & LOGIN ##########################################
#-------------------- create or insert ------------------------------------------------
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

#------------------------ update password -------------------------------------------------------
@app.route('/api/v1/incubator/resources/user/registration/update/<mailid>', methods=['PUT'])
def reg_update(mailid):
    if not request.json:
        abort(404)
    db.create_all()
    user_update = User.query.filter_by(email=str(mailid)).first()
    user_update.password = request.json['psd'] 
    log_update = Login.query.filter_by(login_id=str(mailid)).first()
    log_update.password = request.json['psd']
    db.session.commit()
    print(request.json)
    return "password updated"

#--------------------------- update user ----------------------------------------------------------
@app.route('/api/v1/incubator/resources/user/registration/update/user/<mailid>', methods=['PUT'])
def reg_user_update(mailid):
    db.create_all()

    # update user table
    upd = User.query.filter_by(email=str(mailid)).first()
    upd.name = request.json['name']
    upd.password = request.json['password']
    upd.contact = request.json['contact']
    upd.email = request.json['email']
    upd.company = request.json['company']
    upd.design = request.json['designation']
    upd.why = request.json['why']
    upd.address = request.json['address']

    # update login table
    lo = Login.query.filter_by(login_id=str(mailid)).first()
    lo.login_id = request.json['email']
    lo.password = request.json['password']

    db.session.commit()

    return "user updated"
#------------------------------- delete user ------------------------------------------------------
@app.route('/api/v1/incubator/resources/user/registration/delete/user/<mailid>', methods=['DELETE'])
def user_delete(mailid):
    db.create_all()
    # delete from user table
    d = User.query.filter_by(email=str(mailid)).first()
    db.session.delete(d)
    # delete from login table
    ld = Login.query.filter_by(login_id=str(mailid)).first()
    db.session.delete(ld)
    db.session.commit()
    return "user deleted from user and login table"

#######################################################################################################

########################### Video Insertion into database ##########################################
@app.route('/api/v1/incubator/resources/video/create', methods=['POST'])
def video():
    values = []
    if not request.json:
        return make_response({"json":"NO"})#abort(404)
    for i in request.json:
        values.append(request.json[i])
    
    db.create_all()
    vid = Video(values[0],values[1], values[2], values[3])
    db.session.add(vid)
    db.session.commit()
    return "Inserted into Video table and document table"

#----------------------- Video Updation into database ----------------------------------------------------

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

#--------------------------- Video Deletion from database ----------------------------------------------
@app.route('/api/v1/incubator/resources/video/delete/<int:v_id>', methods=["DELETE"])
def vid_delete(v_id):
    db.create_all()
    # find_doc = Document.query.filter_by()
    de = Video.query.filter_by(id=v_id).first()
    db.session.delete(de)
    db.session.commit()
    return "record deleted\n"

#------------------------ Video: read from database --------------------------------------------------
#-------------------- all data -------------------------
@app.route('/api/v1/incubator/resources/video/read', methods=['GET'])
def vid_get():
    db.create_all()
    # result = db.engine.execute("SELECT * from video")
    jlist = []
    result = Video.query.all()
    for i in result:
        i.__dict__['_sa_instance_state']=str(i.__dict__['_sa_instance_state'])
        jlist.append(i.__dict__)
    print(jlist[0])
    return  jsonify(jlist)

# ------------------ one or few data ------------------------------------------------------------
@app.route('/api/v1/incubator/resources/video/read/id/<int:id>', methods=['GET'])
def vid_getFew(id):
    db.create_all()
    result = Video.query.filter_by(id=int(id)).all()
    # query_parameter = dict(request.args)
    # if 'id' in query_parameter :
    #     id=int(query_parameter.get('id'))
    #     result = Video.query.filter_by(id=id).all()
    jlist = []
    for i in result:
        i.__dict__['_sa_instance_state']=str(i.__dict__['_sa_instance_state'])
        jlist.append(i.__dict__)
    # print(query_parameter)
    return jsonify(jlist)

#######################################################################################################

############################ Document table ##########################################################
#---------------------------- Insert ---------------------------------------------------------

@app.route('/api/v1/incubator/resources/document/insert', methods=['POST'])
def doc_insert():
    db.create_all()
    
    if not request.json:
        return make_response({"json":"NO"})#abort(404)
    find_vid = Video.query.filter_by(video_name=request.json['video_name']).first_or_404(description='there is no data with {}'.format(request.json['video_name']))
    if find_vid:
        new_doc = Document(document_path_url=request.json['doc'], video_name=find_vid)
        db.session.add(new_doc)
    else:
        abort(404)
    db.session.commit()

    return "document inserted"

#-------------------------------- Update ------------------------------------------------------------
@app.route('/api/v1/incubator/resources/document/update', methods=['PUT'])
def doc_update():
    db.create_all()

    if not request.json:
        abort(404)
    
    find_vid = Video.query.filter_by(video_name=request.json['video_name']).first()
    upd_doc = Document.query.filter_by(video_id=find_vid.id).first()
    upd_doc.document_path_url = request.json['doc_path']
    db.session.commit()
    return "document updated"

#--------------------------------- Delete -------------------------------------------------------------
@app.route('/api/v1/incubator/resources/document/delete/<video_name>', methods=['DELETE'])
def doc_delete(video_name):
    db.create_all()

    find_vid = Video.query.filter_by(video_name=str(video_name)).first_or_404(description='record: {} not found'.format(video_name))
    print(find_vid)
    del_doc = Document.query.filter_by(video_id=find_vid.id).first_or_404(description='record: {} not found'.format(video_name))
    print(del_doc)
    db.session.delete(del_doc)
    db.session.commit()
    return "document deleted"

# -----------------------------------GET ----------------------------------------------------------
@app.route('/api/v1/incubator/resources/document/read', methods=['GET'])
def doc_read():
    db.create_all()
    # result = db.engine.execute("SELECT * from video")
    jlist = []
    result = Document.query.all()
    for i in result:
        i.__dict__['_sa_instance_state']=str(i.__dict__['_sa_instance_state'])
        jlist.append(i.__dict__)
    print(jlist[0])
    return  jsonify(jlist)

#######################################################################################################



    
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
