
from myPackage import db

# Class model for user table
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=False, nullable=False)
    password = db.Column(db.String(100),nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    company = db.Column(db.String(30), unique=False, nullable=True)
    design = db.Column(db.String(30), unique=False, nullable=False)
    why = db.Column(db.String(100), unique=False, nullable=True)
    address = db.Column(db.String(100), unique=False, nullable=False)

    def __repr__(self):
        return self.name

#     # one-many relationship with payment_table
#     payments = db.relationship('Payment', backref='user', lazy='dynamic')
#     # one-many relationship with feedback table
#     feedbacks = db.relationship('Feedback', backref='user', lazy='dynamic')
#     # one-one relationship with address table
#     address = db.relationship('Address', backref='user', lazy='dynamic')
    
    
###### class model for login table
class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login_id = db.Column(db.String(100))
    password = db.Column(db.String(100))


# ######## class model for payment table
# class Payment(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     txn_id = db.Column(db.String(100), unique=True, nullable=False)
#     payment_amout = db.Column(db.Float, nullable=False)
#     status = db.Column(db.Boolean,nullable=False)

# ######## class model for feedback table
# class Feedback(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     feedback = db.Column(db.String(500),nullable=True, unique=False)

# ########## class model for address table
# class Address(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
#     addr_line1 = db.Column(db.String(200))
#     addr_line2 = db.Column(db.String(200))
#     country = db.Column(db.String(30), nullable=False,unique=False)
#     state = db.Column(db.String(30), nullable=False, unique=False)
#     city = db.Column(db.String(30), nullable=False, unique=False)



