from databaseFolder import models 
from flask import jsonify

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
    