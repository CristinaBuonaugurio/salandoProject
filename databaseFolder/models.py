from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import bcrypt
from dateutil.parser import parse
db = SQLAlchemy()

class product(db.Model):
    __tablename__ = "product" 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    description = db.Column(db.String(), nullable = False)
    cost = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=1, nullable=False)

    ### Foreigns key
    idcategory = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    ### Relationship 
    users = db.relationship('user', secondary='userbuyproduct', lazy='joined')

    def format(self):
        return {
            'idproduct' : self.id,
            'name' : self.name,
            'description' : self.description,
            'cost' : self.cost,
            'quantity' : self.quantity
        }


class category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(20), nullable = False)

    ### Relantionships
    products = db.relationship('product', backref='product')
    coupons = db.relationship('coupon', backref='category')

    def format(self):
        return {
            'id' : self.id,
            'description' : self.description
        }


class coupon(db.Model):
    __tablename__ = "coupon"
    id = db.Column(db.Integer, primary_key=True)
    endvalidation = db.Column(db.Date, nullable=False)

    ### ForeignKeys 
    iduser = db.Column(db.String(30), db.ForeignKey('users.idmail'), nullable=False)
    idcategory = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def format(self):
        return {
            'id' : self.id,
            'expiring date ': self.endvalidation
        }

class userBuyProduct(db.Model):
    __tablename__ = "userbuyproduct"
    id = db.Column(db.Integer, primary_key=True)
    iduser = db.Column(db.String(30), db.ForeignKey('users.idmail'), primary_key=True)
    idproduct = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    numofprod = db.Column(db.Integer, nullable=False, default=1)
    methodofpayment = db.Column(db.String(30), nullable=False)
    
    ### Relationships
    users = db.relationship('user', backref=("user_assoc"))
    products = db.relationship('product', backref=("product_assoc"))

    def format(self):
        return {
            'id' : self.id,
            'iduser' : self.iduser,
            'idproduct' : self.idproduct,
            'numofproduct' : self.numofprod,
            'methodofpayment' : self.methodofpayment
        }



class admin(db.Model):
    idmail = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    password = db.Column(db.LargeBinary(), nullable=False)

    def __init__(self, idmail, name, surname, birthdate, password):
        self.idmail = idmail
        self.name = name
        self.surname = surname
        self.birthdate = parse(birthdate)
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    def compare(self, passInsert):
        if bcrypt.checkpw(passInsert.encode('utf8'), self.password):
            return True
        else:
            return False


class user(db.Model):
    __tablename__ = "users"
    idmail = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    password = db.Column(db.LargeBinary(60), nullable=False)
    
    def __init__(self,idmail,name,surname,birthdate,password):
        self.idmail = idmail
        self.name = name
        self.surname = surname
        self.birthdate = parse(birthdate)
        self.password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

    def compare(self, passInsert):
        if bcrypt.checkpw(passInsert.encode('utf8'), self.password):
            return True
        else:
            return False

    ### Relationships
    products = db.relationship('product', secondary='userbuyproduct', lazy='joined')
    coupons = db.relationship('coupon', backref='coupon')