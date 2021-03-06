from __future__ import annotations
from abc import abstractmethod
from databaseFolder import functionModels


class templateAcquisto:
    
    def __init__(self):
        self.methodOfPayment = None


    def commitPurchase(self,cliente, value, paymentMethod):
        self.updateQuantityProduct(value)
        self.setMethodOfPayment(paymentMethod)
        self.hasCoupon()
        self.commit(cliente, value)


    
    def updateQuantityProduct(self,value):
        if functionModels.updateQuantity(value): 
            print("Updated Correctly")
       

    def setMethodOfPayment(self, paymentMethod):
        self.methodOfPayment = paymentMethod
            
    def hasCoupon(self):
        print("Sono nei coupon")

    def commit(self,cliente, value):
        product = value['id']
        print(product)
        numofprod = value['numofprod']
        print(numofprod)
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

    def confermaOrdine(self, paymentMethod):
        self.templateAcquisto.commitPurchase(self.cliente, self.value, paymentMethod)
    
    def getValue(self): 
        return self.value


class cartManager:

    def __init__(self, templateAcquisto, cliente):
        self.templateAcquisto = templateAcquisto
        self.cliente = cliente
        self.listOfCarts = []

    def add(self, value) -> None: 
        self.listOfCarts.append(concreteCart(self.templateAcquisto,self.cliente,value))

    def executeAll(self, paymentMethod):
        for cart in self.listOfCarts:
            cart.confermaOrdine(paymentMethod)
        self.removeAll()
    
    def removeAll(self):
        self.listOfCarts.clear()
    
    def remove(self,value):
        for i in range(len(self.listOfCarts)):    
            if value == int(self.listOfCarts[i].getValue()['id']):
                self.listOfCarts.pop(i)
                break
                
    def getNumOfP(self, idproduct):
        cont = 0 
        for cart in self.listOfCarts:
            print(cart.getValue()['id'])
            if idproduct == cart.getValue()['id']:
                cont += 1
        print(cont)
        return cont



    def getCarts(self): 
        carts = [cart.getValue() for cart in self.listOfCarts]
        ###print(carts)
        return carts

