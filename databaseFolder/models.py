from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

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


class category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(20), nullable = False)

    ### Relantionships
    products = db.relationship('product', backref='product')
    coupons = db.relationship('coupon', backref='category')

class coupon(db.Model):
    __tablename__ = "coupon"
    id = db.Column(db.Integer, primary_key=True)
    endvalidation = db.Column(db.Date, nullable=False)

    ### ForeignKeys 
    iduser = db.Column(db.String(30), db.ForeignKey('users.idmail'), nullable=False)
    idcategory = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)



class userBuyProduct(db.Model):
    __tablename__ = "userbuyproduct"
    id = db.Column(db.Integer, primary_key=True)
    iduser = db.Column(db.String(30), db.ForeignKey('users.idmail'), primary_key=True)
    idproduct = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    numofprod = db.Column(db.Integer, nullable=False, default=1)

    ### Relationships
    users = db.relationship('user', backref=("user_assoc"))
    products = db.relationship('product', backref=("product_assoc"))



class admin(db.Model):
    idmail = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    password = db.Column(db.String(10), nullable=False)


class user(db.Model):
    __tablename__ = "users"
    idmail = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    password = db.Column(db.String(10), nullable=False)
    

    ### Relationships
    products = db.relationship('product', secondary='userbuyproduct', lazy='joined')
    coupons = db.relationship('coupon', backref='coupon')