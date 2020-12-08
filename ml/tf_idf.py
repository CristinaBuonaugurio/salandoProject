from databaseFolder import functionModels as f 
from flask import jsonify
from math import log
def method():
    return jsonify(calcute_tfidf())

def calcute_tfidf():
    distinctClients = f.getClients()  ### get distinct clients, meaning only the users that have bought at least one product
    clientsPerProducts = {}  ### Create a dictionary that it will contain as key a client and as value another dictionary
                             ### in which the key is the id of product and the value the number of items of that product
    for d in distinctClients:
        clientsPerProducts[d] = f.getBuyProductsByUsers(d)
        #print(clientsPerProducts)
    
    productsRarity = {}
    for client, purchases in clientsPerProducts.items(): ### iterating to calculate the frequency of each item bought by the users
        numOfPurchases = len(purchases)
        for p in purchases.keys():   ### iterating the products and calculate their frequency 
            temp = purchases[p]
            purchases[p] /= float(numOfPurchases)
            
            if p in productsRarity:     ###get in this new dictionary how many times a product is in a purchase
                productsRarity[p] += temp
            else:
                productsRarity[p] = temp

    numOfClients = len(distinctClients)
    
    for ir in productsRarity.keys():
        productsRarity[ir] = float(numOfClients) / productsRarity[ir]
        productsRarity[ir] = log(productsRarity[ir])

    for c, p in clientsPerProducts.items():
        for i in p.keys():
            p[i] *= productsRarity[i]
            
    
    return clientsPerProducts