from databaseFolder import models 
from flask import jsonify
from sqlalchemy import distinct, func
import datetime

### begin functions for model category

def getCategories(routeRequest = None):
    categories = models.category.query.all()
    results = {}
    for c in categories:
        results[c.id] = c.description
    
    if routeRequest is not None:          
        return jsonify(results)
    else:
        return results


def getCategory(id, routeRequest = None):
    cat = models.category.query.get(id)
    results = []
    for c in cat:
         results.append(c.id)
         results.append(c.description)
    
    if routeRequest is not None:          
        return jsonify(results)
    else:
        return results


### end functions for model category 
###
###
### begin functions for model product


def getAllProducts(routeRequest = None):
    products = models.product.query.all()
    results = []
    for p in products:
        results.append(p.id)
        results.append(p.name)
        results.append(p.description)
        results.append(p.cost)
        results.append(p.quantity)
        results.append(p.idcategory)  
    
    if routeRequest is not None:          
        return jsonify(results)
    else:
        return results
    
def getProductsById(id, routeRequest = None):
    p = models.product.query.get(id)
    results = []
    results.append(p.id)
    results.append(p.name)
    results.append(p.description)
    results.append(p.cost)
    results.append(p.quantity)
    results.append(p.idcategory) 

    if routeRequest is not None:          
        return jsonify(results)
    else:
        return results

def getProductsByCategory(idcategory, routeRequest=None):
    products = models.product.query.filter_by(idcategory = idcategory).all()
    results = []
    for p in products:
        results.append(p.id)
        results.append(p.name)
        results.append(p.description)
        results.append(p.cost)
        results.append(p.quantity)
        results.append(p.idcategory)

    if routeRequest is not None:          
        return jsonify(results)
    else:
        return results 

def insertNewProduct( name, description, category, cost, quantity=1, routeRequest=None):
    p = models.product(name=name, description=description, cost=cost, quantity=quantity, idcategory=category)
    models.db.session.add(p)
    models.db.session.commit()

    return jsonify("Bella fra.")


### end functions for model product 
###
###
### begin functions for model userbuyproduct

def getBuyProductsByUsers(client, routeRequest=None):
    productsB = models.userBuyProduct.query.filter_by(iduser=client).all()
    results = []
    if len(productsB) > 1:
        for p in productsB:
            results.append(p.idproduct)
            results.append(p.numofprod)
    else:
        msg = "There is no products"
        return jsonify(msg)

    if routeRequest is not None:          
        return jsonify(results)
    else:
        return results   

def getClients(routeRequest=None):
    usersB = models.userBuyProduct.query.with_entities(models.userBuyProduct.iduser).distinct().all()
    results = []
    print(usersB)
    if len(usersB) > 1:
        for u in usersB:
            results.append(u.iduser)
    else:
        msg = "There is no users"
        return jsonify(msg)
    
    if routeRequest is not None:
        return jsonify(results)
    else:
        return results

def getNumBuyOfProduct(idproduct, routeRequest=None):
    numCount = 0
    numCount = models.userBuyProduct.query.filter_by(idproduct=idproduct).count()
    results = []
    if numCount > 0:
        results.append(str(numCount))
    else:
        msg = "There are none of it"
        return jsonify(msg)
    
    if routeRequest is not None:
        return jsonify(results)
    else:
        return results


### end functions for model userbuyproduct 
###
###
### begin functions for model coupon

def checkCoupon(iduser, routeRequest=None):
    rs = models.coupon.query.filter_by(iduser=iduser).first()
    results = []
    if rs is not None:
        results.append(rs.id)
        results.append(r.idcategory)
    else:
        msg = "There is none."
        return jsonify(msg)
    
    if routeRequest is not None:
        return jsonify(results)
    else:
        return results

def insertCoupon( idcategory, iduser, routeRequest=None):
    rs = models.coupon.query.filter_by(iduser=iduser).first()
    if rs is None:
        endVal = datetime.datetime.now()
        ###endVal = datetime.datetime.now() + datetime.timedelta(30)
        newcoupon = models.coupon(endvalidation=endVal, iduser=iduser, idcategory=idcategory)
        models.db.session.add(newcoupon)
        models.db.session.commit()
    return jsonify("Fine.")
        
### end functions for model coupon 
###
###
### begin functions for model users

def registerNewUser(mail, name, surname, birthdate, password, routeRequest=None):
    newUser = models.user(idmail=mail, name=name, surname=surname, birthdate=birthdate, password=password)
    models.db.session.add(newUser)
    models.db.session.commit()
    return jsonify("Grande sei registrato!")