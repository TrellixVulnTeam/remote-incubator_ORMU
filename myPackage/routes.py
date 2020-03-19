from flask import jsonify, request, abort, make_response, render_template, request
from myPackage.models.user import User, Login, Feedback, Payment, Address, Subscription
from myPackage.models.gallery import Video, Document
from myPackage import app, db, bcrypt
from myPackage.models import razorpay_key

from myPackage.models.order_id import OrderId

from myPackage.mail.generateMail import sendMailTo

import json
import datetime
import jwt
import requests

##### Allow database functionality ###########
db.create_all()
############################################

##################### home ##########################################################################
@app.route('/')
@app.route('/home')
def index():
    return make_response({'Hi':'REmote incubator'})

###################################################################################################

########################## user REGISTRATION & LOGIN ##########################################
#-------------------- create or insert ------------------------------------------------
@app.route('/api/v1/incubator/resources/user/registration/create',methods=['POST'])
def regis():
    # db.create_all()
    ########## user validation #####################3
    find_user = User.query.filter_by(email=request.json['email']).first()
    if find_user:
        return make_response({'sorry':'someone already registered with this email'}), 405
     ##############################################   
    
    if not request.json:
        return make_response({'oops':'no json data provided'})
    
    values = []
    for i in request.json:
        values.append(request.json[i])
    # print(values)
    # Adding to user table
    new_user = User(name=values[0],contact=values[2],email=values[3],company=values[4],design=values[5],why=values[6],address=values[7])
    db.session.add(new_user)
    uid = new_user.user_id
    print(new_user.__dict__)
    
    # Adding to login table
    log = Login(login_id=new_user.email, password=values[1], user=new_user)
    print(log)
    
    db.session.add(log)
    db.session.commit()
    return jsonify({'succeed':"value inserted in user and login tables"}), 201

#------------------------ update password -------------------------------------------------------
@app.route('/api/v1/incubator/resources/user/registration/update/<mailid>', methods=['PUT'])
def reg_update(mailid):
    if not request.json:
        abort(404)
    # db.create_all()
    user_update = Login.query.filter_by(login_id=str(mailid)).first()
    # validate user
    if not user_update:
        return make_response({'OOPS':'Invalid email'})
    user_update.password = request.json['psd'] 
    # log_update = Login.query.filter_by(login_id=str(mailid)).first()
    # log_update.password = request.json['psd']
    db.session.commit()
    print(request.json)
    return jsonify({'succeed':'password updated'})

#--------------------------- update user (update everything)----------------------------------------------------------
@app.route('/api/v1/incubator/resources/user/registration/update/user/<mailid>', methods=['PUT'])
def reg_user_update(mailid):
    # db.create_all()

    # update user table
    upd = User.query.filter_by(email=str(mailid)).first()
    # validating upd
    if not upd:
        return jsonify({'sorry':'no data found'})
    upd.name = request.json['name']
    upd.contact = request.json['contact']
    upd.email = request.json['email']
    upd.company = request.json['company']
    upd.design = request.json['designation']
    upd.why = request.json['why']
    upd.address = request.json['address']
    # update password in login table
    log = Login.query.filter_by(login_id=request.json['email'])
    if not log:
        return jsonify({'Sorry':'No date found'})

    log.password = request.json['password']

    db.session.commit()

    return jsonify({'database':'user updated'}), 200 # or 204
#------------------------------- delete user ------------------------------------------------------
@app.route('/api/v1/incubator/resources/user/registration/delete/user/<mailid>', methods=['DELETE'])
def user_delete(mailid):
    # db.create_all()
    # delete from user table
    d = User.query.filter_by(email=str(mailid)).first()
    if not d:
        return jsonify({'sorry':'no user found'})
    db.session.delete(d)
    # delete from login table
    ld = Login.query.filter_by(login_id=str(mailid)).first()
    db.session.delete(ld)
    db.session.commit()
    return jsonify({'succeed':"user deleted from user and login table"})

#----------------------------------- Read user ---------------------------------------------------
@app.route('/api/v1/incubator/resources/registration/read', methods=['GET'])
def user_read():
    # db.create_all()
    result = db.engine.execute("SELECT * from video")
    jlist = []
    result = User.query.all() 
    print("this is from database: ",result)
    print(result)
    
    for i in result:
        i.__dict__['_sa_instance_state']=str(i.__dict__['_sa_instance_state'])
        i.__dict__.pop('_sa_instance_state')
        jlist.append(i.__dict__)
    print(jlist[0])
    return  jsonify(jlist)

############################## Feedback table ########################################################

#---------------------------------- POST service ----------------------------------------------------
@app.route('/api/v1/incubator/resources/feedback/insert', methods=['POST'])
def feedbk_insert():
    # db.create_all()
    if not request.json:
        abort(404)
    find_user = User.query.filter_by(user_id=request.json['user_id']).first_or_404(description="user not found")
    # print(find_user)
    if find_user:
        new_feedback = Feedback(feedback=request.json['feedback'], user=find_user)
        db.session.add(new_feedback)
    else:
        abort(404)
    db.session.commit()

    return "feedback inserted"

#------------------------------------ PUT service -----------------------------------------------------
@app.route('/api/v1/incubator/resources/feedback/update', methods=['PUT'])
def feedbk_update():
    # db.create_all()
    upd = Feedback.query.filter_by(user_id=request.json['user_id']).first()
    upd.feedback = request.json['feedback']
    db.session.commit()

    return "Feedback updated"

#-----------------------------------DELETE service ---------------------------------------------------
@app.route('/api/v1/incubator/resources/feedback/delete/<int:id>', methods=['DELETE'])
def feedbk_delete(id):
    # db.create_all
    de_fb = Feedback.query.filter_by(user_id=id).first()
    db.session.delete(de_fb)
    db.session.commit()

    return "feedback deleted"

#------------------------------------- GET service ---------------------------------------------------
@app.route('/api/v1/incubator/resources/feedback/read', methods=['GET'])
def feedbk_read():
    # db.create_all()
    # result = db.engine.execute("SELECT * from video")
    jlist = []
    result = Feedback.query.all()
    for i in result:
        i.__dict__['_sa_instance_state']=str(i.__dict__['_sa_instance_state'])
        jlist.append(i.__dict__)
    print(jlist[0])
    return  jsonify(jlist)

######################################################################################################


#---------------------------- Insert ---------------------------------------------------------

@app.route('/api/v1/incubator/resources/payment/insert', methods=['POST'])
def pay_insert():
    # db.create_all()
    
    if not request.json:
        return make_response({"json":"NO"})#abort(404)
    find_user = User.query.filter_by(user_id=request.json['user_id']).first_or_404(description='there is no data with {}'.format(request.json['user_id']))

    if find_user:
        new_pay = Payment(txn_id=request.json['txn'], payment_amout=request.json['pay_amout'],status=request.json['status'], user=find_user)
        db.session.add(new_pay)
    else:
        abort(404)
    db.session.commit()

    return "payment made successfully"

#-------------------------------- Update ------------------------------------------------------------
@app.route('/api/v1/incubator/resources/payment/update', methods=['PUT'])
def pay_update():
    # db.create_all()

    if not request.json:
        abort(404)
    
    find_user = User.query.filter_by(user_id=request.json['user_id']).first_or_404(description='record not found')
    upd_pay = Payment.query.filter_by(user_id=find_user.user_id).first()
    upd_pay.payment_amout = request.json['pay_amout']
    upd_pay.status = request.json['status']
    db.session.commit()
    return "payment updated"

#--------------------------------- Delete -------------------------------------------------------------
@app.route('/api/v1/incubator/resources/payment/delete/<id_>', methods=['DELETE'])
def pay_delete(id_):
    # db.create_all()

    find_user = User.query.filter_by(user_id=int(id_)).first_or_404(description='record: not found')
    # print(find_vid)
    del_pay = Payment.query.filter_by(user_id=find_user.user_id).first_or_404(description='record: {} not found')
    print(del_pay)
    db.session.delete(del_pay)
    db.session.commit()
    return "payment deleted"

# -----------------------------------GET ----------------------------------------------------------
@app.route('/api/v1/incubator/resources/payment/read', methods=['GET'])
def pay_read():
    # db.create_all()
    # result = db.engine.execute("SELECT * from video")
    jlist = []
    result = Payment.query.all()
    print(result)
    for i in result:
        i.__dict__['_sa_instance_state']=str(i.__dict__['_sa_instance_state'])
        jlist.append(i.__dict__)
    return  jsonify(jlist)

#######################################################################################################


#################################### ADDRESS TABLE ####################################################
#---------------------------- Insert ---------------------------------------------------------

@app.route('/api/v1/incubator/resources/address/insert', methods=['POST'])
def addr_insert():
    # db.create_all()
    values=[]
    if not request.json:
        return make_response({"json":"NO"})#abort(404)
    else:
        for i in request.json:
            values.append(request.json[i])

    find_user = User.query.filter_by(user_id=values[0]).first_or_404(description='there is no data with {}'.format(values[0]))

    if find_user:
        add_addr = Address(addr_line1=values[1], addr_line2=values[2], country=values[3], state=values[4], city=values[5], user=find_user)
        db.session.add(add_addr)
    else:
        abort(404)
    db.session.commit()

    return "Address inserted"

#-------------------------------- Update ------------------------------------------------------------
@app.route('/api/v1/incubator/resources/address/update', methods=['PUT'])
def addr_update():
    # db.create_all()

    if not request.json:
        abort(404)
    
    find_user = User.query.filter_by(user_id=request.json['user_id']).first_or_404(description='record not found')
    upd = Address.query.filter_by(user_id=find_user.user_id).first()
    upd.addr_line1 = request.json['addr1']
    upd.addr_line2 = request.json['addr2']
    upd.country = request.json['country']
    upd.state = request.json['state']
    upd.city = request.json['city']
    db.session.commit()
    return "Address updated"

#--------------------------------- Delete -------------------------------------------------------------
@app.route('/api/v1/incubator/resources/address/delete/<id_>', methods=['DELETE'])
def addr_delete(id_):
    # db.create_all()

    find_user = User.query.filter_by(user_id=int(id_)).first_or_404(description='record: not found')
    
    del_addr = Address.query.filter_by(user_id=find_user.user_id).first_or_404(description='record: {} not found')
    
    db.session.delete(del_addr)
    db.session.commit()
    return "address deleted"

# -----------------------------------GET ----------------------------------------------------------
@app.route('/api/v1/incubator/resources/address/read', methods=['GET'])
def addr_read():
    # db.create_all()
    # result = db.engine.execute("SELECT * from video")
    jlist = []
    result = Address.query.all()
    print(result)
    for i in result:
        i.__dict__['_sa_instance_state']=str(i.__dict__['_sa_instance_state'])
        jlist.append(i.__dict__)
    return  jsonify(jlist)

######################################################################################################

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

@app.route('/api/v1/incubator/resources/video/update', methods=['PUT'])
def vid_update():
    # db.create_all()
    print(request.json)
    upd = Video.query.filter_by(video_name=request.json['video_name']).first_or_404(description='record')
    if not request.json:
        abort(404)
    print(type(request.json))
    upd.video_name = request.json['video_name']
    upd.video_url = request.json['video_url']
    upd.description = request.json['description']
    upd.category = request.json['category'] #request.json.get("category",upd.category)
    db.session.commit()
    return "sucess"

#--------------------------- Video Deletion from database ----------------------------------------------
@app.route('/api/v1/incubator/resources/video/delete/<int:v_id>', methods=["DELETE"])
def vid_delete(v_id):
    print(type(v_id))
    db.create_all()
    # find_doc = Document.query.filter_by()
    de = Video.query.filter_by(id=v_id).first()
    
    # delete related documents
    docs = Document.query.filter_by(video_id=de.id).delete()
    print(docs)
    # db.session.delete(docs)
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


######################################## PAYMENT GATEWAY route ##############################################
# ------------------------------- generate order id ---------------------------------------------------
@app.route('/api/v1/incubator/resources/orderid', methods=['POST'])
def orderid():
    # POST method is used when we use this route as api
    DATA={'amount':1000,'currency':'INR','receipt':"my_recept",'payment_capture':0}
    item = OrderId(DATA)
    item = item.get_with_id()
    convert_to_json_item = json.dumps(item)
    json_item = json.loads(convert_to_json_item)
    # print(json_item)
    return str(json_item)

#---------------------------------------------------------------------------------------------------

#---------------------------------------- Payment making --------------------------------------------------------
# user detail should be fetched from user session, like user id. (here user_id =1 has been used)
@app.route('/payment')
def pay():
    key = razorpay_key
    # print(key)
    if not key:
        return jsonify({'sorry':'not gateway api key'})
    oid = orderid()
    # print(oid)
    if not oid:
        return jsonify({'sorry':'not order id'})

    # validating user
    find_user = User.query.filter_by(user_id=1).first()
    if not find_user:
        return jsonify({'sorry':'not found'}), 404

    return render_template('pay.html',key=key,oid=oid)

@app.route('/payment/success', methods=['POST'])
def successPay():
    if not request.form:
        return jsonify({'sorry':'No form fetched'})
    
    # Adding to subscription table
    # Extract detail from form
    email = 'hbr8218@gmail.com'
    find_user = User.query.filter_by(email=email).first()

    start_date = datetime.datetime.now().date()#datetime.datetime.strptime(values[8], '%Y-%m-%d').date()
    end_date = start_date + datetime.timedelta(days=365)
    subs = Subscription(subs_start=start_date, subs_end=end_date, status=1, user=find_user)
    
    db.session.add(subs)
    db.session.commit()

    
    # send registration mail to user
    
    print("receiver email address: ",email)
    sendMailTo(email)

    return jsonify({'status':"Payment successful"})
    
########################################################################################################
