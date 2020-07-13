from . import db
from werkzeug.security import generate_password_hash,check_password_hash



class User (db.Model):
    """ User model """

    __tablename__ = "users"
    

    def __repr__(self):
        return f'User {self.username}'



class Pitches (db.Model):
    """ Pitches model """

    __tablename__ = "pitches"
    id = db.Column(db.Integer,primary_key = True)
    category = db.Column(db.String(255),index = True)
    pitch = db.Column(db.String(255),unique = True,index = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comments',backref = 'pitch',lazy ='dynamic')



    def __repr__(self):
        return f'Pitches {self.pitch}'

class Comments (db.Model):
    """ Comments model """

    __tablename__ = "comments"
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255),index = True)
    pitches_id = db.Column(db.Integer,db.ForeignKey("pitches.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

