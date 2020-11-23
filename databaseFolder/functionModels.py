from databaseFolder import models 
from flask import jsonify
from sqlalchemy import distinct, func
import datetime
import random
import sys
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


def updateQuantityProduct(idproduct, quantityUpdate):
    status = False
    try:
        if quantityUpdate >= 0:
            models.db.session.query(models.product).filter_by(id=idproduct).update({'quantity': quantityUpdate})
            models.db.session.commit()
            status = True
    except:
        models.db.session.rollback()
    finally:
        models.db.session.close()
    return status

def updateDescriptionProduct(idproduct, description):
    status = False
    try:
        models.db.session.query(models.product).filter_by(id=idproduct).update({'description': description})
        models.db.session.commit()
        status = True
    except:
        models.db.session.rollback()
    finally:
        models.db.session.close()
    return status


### end functions for model product 
###
###
### begin functions for model userbuyproduct

def getBuyProductsByUsers(client, routeRequest=None):
    productsB = models.userBuyProduct.query.filter_by(iduser=client).all()
    dict = {}
    if len(productsB) >= 1:
        for p in productsB:
            if p.idproduct in dict:
                 dict[p.idproduct] += p.numofprod
            else:     
                dict[p.idproduct] = p.numofprod 
    else:
        if routeRequest is not None:  
            msg = "There is no products"
            return jsonify(msg)
        else:
            return None
    
    if routeRequest is not None:  
        msg = "There is no products"
        return jsonify(msg)
    else:
        return dict



def getClients():
    usersB = models.userBuyProduct.query.with_entities(models.userBuyProduct.iduser).distinct().all()
    results = []
    if len(usersB) >= 1:
        for u in usersB:
            results.append(u.iduser)
    else:
        msg = "There is no users"
        print(msg)
        return results
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

def buyProducts(client, product, numofprod):
    purchase = models.userBuyProduct(id=random.randint(0,10000),iduser=client, idproduct = product, numofprod =numofprod)
    models.db.session.add(purchase)
    models.db.session.commit()
    return jsonify("The client {} has bought the product with id: {}".format(client, product))



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

def insertCoupon(idcategory, iduser, routeRequest=None):
    rs = models.coupon.query.filter_by(iduser=iduser).first()
    if rs is None:
        endVal = datetime.datetime.now()
        ###endVal = datetime.datetime.now() + datetime.timedelta(30)
        newcoupon = models.coupon(endvalidation=endVal, iduser=iduser, idcategory=idcategory)
        models.db.session.add(newcoupon)
        models.db.session.commit()
    return jsonify("Fine.")

def checkOldCoupon():
    oldDate = datetime.datetime.now()
    models.db.session.query(models.coupon).filter(models.coupon.endvalidation < oldDate).delete()
    models.db.session.commit()
    return jsonify("Fine.")

def deleteCoupon(idcliente,routeRequest=None):
    models.coupon.query.filter_by(iduser = idcliente).delete()
    models.db.session.commit()
    return jsonify("Deleted")


### end functions for model coupon 
###
###
### begin functions for model users

def registerNewUser(mail, name, surname, birthdate, password, routeRequest=None):
    newUser = models.user(idmail=mail, name=name, surname=surname, birthdate=birthdate, password=password)
    models.db.session.add(newUser)
    models.db.session.commit()
    return jsonify("Grande sei registrato!")


def getAllUsers(routeRequest=None):
    rs = models.user.query.all()
    results = []
    return jsonify(results)