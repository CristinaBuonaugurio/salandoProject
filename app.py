from databaseFolder import models, functionModels
from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_migrate import Migrate
from ml import tf_idf as t
from datetime import datetime
from flask_cors import CORS
from purchaseManagement import client

app = Flask(__name__, instance_relative_config=True) #create a flask application
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://Cristina@localhost:5432/salando'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

models.db.init_app(app)
migrate = Migrate(app, models.db)

###CORS HEADERS
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type Authorization, true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, PATCH, DELETE, OPTIONS')
    return response


@app.route('/')
def main_page():
    return render_template('login.html')


@app.route('/shop', methods = ['GET'])
def shop():
    products = models.product.query.order_by(models.product.idcategory).all()
    formatted_products = [p.format() for p in products ]
    return render_template("shop.html", data=formatted_products)

@app.route('/magazine')
def magazine_page():
    return render_template('magazine.html')

@app.route('/products', methods = ['GET'])
def products():
    products = models.product.query.all()
    formatted_products = [p.format() for p in products ]
    return jsonify({
        'success' : True,
        'products'  : formatted_products
    })

@app.route('/shop/cart', methods = ['GET'])
def getshoppingcart():
    body = request.get_json()
    mail = body.get['mail']


@app.route('/categories', methods = ['GET'])
def categories():
    return functionModels.getCategories('route')

@app.route('/products/<id_category>', methods = ['GET'])
def getProductByCategory(id_category):
    return functionModels.getProductsByCategory(id_category,'route')
    

@app.route('/registration')
def mainRegistration():
    return render_template('registration.html')



@app.route('/registrationForm', methods = ['POST'])
def registrationUser():
    body = request.get_json()
    mail = body.get('mail')
    name = body.get('name')
    surname = body.get('surname')
    birthdate = body.get('birthdate')
    password = body.get('password')

    newuser = models.user(idmail=mail, name=name, surname=surname,birthdate= birthdate, password=password)
    print(newuser)
    try: 
        models.db.session.add(newuser)
        models.db.session.commit()
        return jsonify({
            'success' : True
        })
    except:
        models.db.session.rollback()
        abort(500)
    finally:
        models.db.session.close()


@app.route('/login', methods = ['POST'])
def login():
    body = request.get_json()
    mail = body.get('mail')
    password = body.get('password')
    
    ###Let's see if there is an user with that mail
    try:
        result = models.user.query.get(mail)
        if result is not None:
            if result.compare(password):
                return jsonify({
                    "success" : True,
                    "mail" : mail, 
                    "role" : "client"
                })
            else:
                return jsonify({
                    "success" : False
                })
        else:
            result = models.admin.query.get(mail)
            if result is not None:
                if result.compare(password):
                    return jsonify({
                        "success" : True,
                        "mail" : mail,
                        "role" : "admin"
                    })
                else:
                    return jsonify({
                        "success" : False
                    })
    except:
        models.db.session.rollback()
    finally:
        models.db.session.close()




@app.route('/amministration/products', methods = ['POST'])
def createProduct():
    body = request.get_json()

    name = body.get('name')
    description = body.get('description')
    cost = int(body.get('cost'))
    quantity = int(body.get('quantity'))
    category = int(body.get('category'))
    newproduct = models.product(name=name, description=description, cost=cost, quantity=quantity, idcategory=category)
    try:
        models.db.session.add(newproduct)
        models.db.session.commit()
        return jsonify({
            'success' : True
        })
    except:
        models.db.session.rollback()
        abort(500)
    finally:
        models.db.session.close()


@app.route('/amministration/products/description/<idProduct>', methods = ['POST'])
def updateDescription(idProduct):
    id = int(idProduct)
    newdescription = request.get_json()['description']
    status = functionModels.updateDescriptionProduct(id, newdescription)
    if status:
        return jsonify({
            "success" : True
        })
    else:
        return jsonify({
            "success" : False
        }) 


@app.route('/amministration/products/quantity/<idProduct>', methods = ['POST'])
def updateQuantity(idProduct):
    id = int(idProduct)
    newquantity = int(request.get_json()['quantity'])
    status = functionModels.updateQuantityProduct(id, newquantity)
    if status:
        return jsonify({
            "success" : True
        })
    else:
        return jsonify({
            "success" : False
        })

### Following error handling

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success" : False,
        "error" : 500, 
        "message" : "Couldn't process the request"
    }), 500
