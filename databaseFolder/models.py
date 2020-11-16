from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


class product(db.Model):
    __tablename__ = "product" 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable = False)
    description = db.Column(db.String(), nullable = False)
    cost = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=1)

    ### Foreigns key
    idCategory = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    
    ### Relationship 
    users = db.relationship('user', secondary='userbuyproduct', lazy='joined')



class category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(20), nullable = False)

    products = db.relationship('products', backref='product')
    coupons = db.relationship('couponsAssociated', backref='category')



class coupon(db.Model):
    __tablename__ = "coupon"
    id = db.Column(db.Integer, primary_key=True)
    endValidation = db.Column(db.Date, nullable=False)

    ### ForeignKeys 
    idUser = db.Column(db.String(30), db.ForeignKey('user.id'), nullable=False)
    idCategory = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)



class userBuyProduct(db.Model):
    __tablename__ = "userbuyproduct"
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.String(30), db.ForeignKey('user.idMail'), primary_key=True)
    idProduct = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    numOfProd = db.Column(db.Integer, nullable=False, default=1)

    users = db.relationship('user', backref=("user_assoc"))
    products = db.relationship('product', backref=("product_assoc"))



class admin(db.Model):
    idMail = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    birthDate = db.Column(db.Date, nullable=True)
    password = db.Column(db.String(10), nullable=False)


class user(db.Model):
    __tablename__ = "user"
    idMail = db.Column(db.String(30), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(30), nullable=False)
    birthDate = db.Column(db.Date, nullable=True)
    password = db.Column(db.String(10), nullable=False)
    

    ### Relationships
    products = db.relationship('product', secondary='userbuyproduct', lazy='joined')
    
    coupons = db.relationship('coupons', backref='coupon')

