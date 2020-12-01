from __future__ import annotations
from abc import abstractmethod
from databaseFolder import functionModels


class templateAcquisto:
    
    def __init__(self):
        self.methodOfPayment = None


    def commitPurchase(self,cliente, value):
        self.updateQuantityProduct(value)
        self.setMethodOfPayment()
        self.hasCoupon()
        self.commit(cliente, value)


    
    def updateQuantityProduct(self,value):
        if functionModels.updateQuantity(value): 
            print("Updated Correctly")
       
    def changeMethodPayment(self, newmp):
        self.methodOfPayment = newmp

    def setMethodOfPayment(self):
        self.methodOfPayment = "CONTANTI" 
            
    def hasCoupon(self):
        print("Sono nei coupon")

    def commit(self,cliente, value):

        product = list(value.keys())[0]
        print(product)
        numofprod = value[product]
        functionModels.buyProducts(cliente, product, numofprod , self.methodOfPayment)


class InterfaceCart():

    @abstractmethod
    def confermaOrdine(self) -> None:
        pass


class concreteCart(InterfaceCart):

    def __init__(self, templateAcquisto, cliente, value): 
        self.templateAcquisto = templateAcquisto
        self.cliente = cliente
        self.value = value ### It has to be a dictionary with key id product and value the number of that product

    def confermaOrdine(self):
        self.templateAcquisto.commitPurchase(self.cliente, self.value)
    
    def getValue(self): 
        return self.value


class cartManager:

    def __init__(self, templateAcquisto, cliente):
        self.templateAcquisto = templateAcquisto
        self.cliente = cliente
        self.listOfCarts = []

    def add(self, value) -> None: 
        self.listOfCarts.append(concreteCart(self.templateAcquisto,self.cliente,value))

    def executeAll(self):
        for cart in self.listOfCarts:
            cart.confermaOrdine()
    
    def removeAll():
        self.listOfCarts.clear()
    
    def remove(value):
        self.listOfCarts.remove(value)

    def getCarts(self): 
        carts = [cart.getValue() for cart in self.listOfCarts]
        ###print(carts)
        return carts

