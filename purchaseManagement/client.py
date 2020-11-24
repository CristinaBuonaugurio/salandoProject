from purchaseManagement import purchase



class currentUser:

    def __init__(self, idmail):
        self.idmail = idmail
        self.templateacquisto = purchase.templateAcquisto()
        self.manager = purchase.cartManager(templateAcquisto=self.templateacquisto, cliente=self.idmail)

    def getCarts():
        return self.manager.getCarts()  

    def addProduct(self, idproduct, numofprod): 
        dict = {}
        dict[idproduct] = numofprod
        self.manager.add(value=dict)

    def definitivepurchase(self) -> None:
        self.manager.executeAll()
    
