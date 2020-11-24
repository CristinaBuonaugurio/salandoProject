from __future__ import annotations
from abc import abstractmethod

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
        templateAcquisto.commitAcquisti(cliente, value)


class cartManager:

    def __init__(self, templateAcquisto, cliente):
        self.templateAcquisto = templateAcquisto
        self.cliente = cliente
        self.listOfCarts = []

    def add(value): 
        listOfCarts.add(InterfaceCart(templateAcquisto,cliente,value))

    def executeAll():
        for cart in listOfCarts:
            cart.confermaOrdine()
    
    def removeAll():
        listOfCarts.clear()
    
    def remove(value):
        listOfCarts.remove(value)


