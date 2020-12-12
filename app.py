from databaseFolder import models, functionModels
from flask import Flask, jsonify, request, redirect, url_for, render_template, session
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




global currentClientLogged 


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
    global currentClientLogged
    products = models.product.query.order_by(models.product.idcategory).all()
    formatted_products = [p.format() for p in products if (p.quantity - currentClientLogged.getNumOfP(p.id)) > 0]
    return render_template('shop.html', data=formatted_products)

@app.route('/magazine')
def magazine_page():
    products = models.product.query.all()
    formatted_products = [p.format() for p in products]
    return render_template('magazine.html', data=formatted_products)


@app.route('/shop/<idcat>', methods = ['GET'])
def getCateg(idcat):
    global currentClientLogged
    products = functionModels.getProductsByCategory(int(idcat))
    formatted_products = [p.format() for p in products if (p.quantity - currentClientLogged.getNumOfP(p.id)) > 0]
    return render_template('shop.html', data=formatted_products)



@app.route('/shop/cart', methods = ['GET'])
def getshoppingcart():
    global currentClientLogged
    if isinstance(currentClientLogged, client.currentUser):
        items = currentClientLogged.getCarts()
    else:
        items = {}
        items['countItem'] = 0
    return render_template('cart.html', data=items)


@app.route('/categories', methods = ['GET'])
def categories():
    return functionModels.getCategories('route')

@app.route('/products/<id_category>', methods = ['GET'])
def getProductByCategory(id_category):
    return functionModels.getProductsByCategory(id_category,'route')
    

@app.route('/registration')
def mainRegistration():
    return render_template('registration.html')

@app.route('/shop/cart/delete', methods = ['DELETE'])
def delProduct(): 
    global currentClientLogged
    body = request.get_json()
    idproduct = int(body.get('id'))
    currentClientLogged.removeProduct(idproduct)
    print(currentClientLogged.getCarts())
    return jsonify({
        'success' : True
    })


@app.route('/shop/cart/empty', methods = ['DELETE'])
def emptyCart(): 
    global currentClientLogged
    currentClientLogged.emptyProducts()
    return jsonify({
        'success' : True
    })

@app.route('/shop/cart/confirm', methods = ['POST'])
def confirmPurchase(): 
    body = request.get_json()
    methodOfP = body.get('paymentmethod')
    global currentClientLogged
    currentClientLogged.definitivepurchase(methodOfP)
    return jsonify({
        'success' : True
    })

@app.route('/shop/add', methods = ['POST'])
def addProduct(): 
    global currentClientLogged
    body = request.get_json()
    mailClient = body.get('mail')
    idproduct = int(body.get('id'))
    numofprod = int(body.get('numOfProd'))  
    idname = body.get('name')  
    currentClientLogged.addProduct(idproduct = idproduct, numofprod=numofprod, name=idname)
    return jsonify({
        'success' : 'true'
    })


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


@app.route('/profile')
def profileOverview():
    data = currentClientLogged.getMyProfile()
    return render_template('profile.html', data=data)


@app.route('/login', methods = ['POST'])
def login():
    body = request.get_json()
    mail = body.get('mail')
    password = body.get('password')
    global currentClientLogged
    ###Let's see if there is an user with that mail
    try:
        result = models.user.query.get(mail)
        if result is not None:
            if result.compare(password):
                currentClientLogged = client.currentUser(idmail=mail)
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




@app.route('/magazine/products', methods = ['POST'])
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


@app.route('/magazine/modifyProduct', methods = ['POST'])
def updateProduct(): 
    body = request.get_json()
    idproduct = int(body['id'])
    description = str(body['description'])
    quantity = int(body['quantity'])
    print(description)
    if quantity == 0 and description != "":
        status = functionModels.updateDescriptionProduct(idproduct, description)
        if status:
           
            return jsonify({
                "success" : True
            })
        else:
            return jsonify({
                "success" : False
            })
    elif quantity !=0 and description == "":
        status = functionModels.updateQuantityProduct(idproduct, quantity)
        if status:
            return jsonify({
                "success" : True
            })
        else:
            return jsonify({
                "success" : False
            })
    else:
        status1 = functionModels.updateDescriptionProduct(idproduct, description)
        status = functionModels.updateQuantityProduct(idproduct, quantity)
        if status1 and status: 
            return jsonify({
                "success" : True
            })
        else:
            return jsonify({
                "success" : False
            })
       


@app.route('/magazine/tfidf')
def tfidfShow():
    return t.method()



### Following error handling

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({
        "success" : False,
        "error" : 500, 
        "message" : "Couldn't process the request"
    }), 500
    



if __name__ == "_main_":
    app.run()