import purchaseManagement



class currentUser:
    def __init__(self, idmail):
        self.idmail = idmail
        self.templateacquisto = templateAcquisto()
        self.manager = cartManager(templateacquisto, idmail)


    def getCarts():
        return manager.getCarts()  

    def addProduct(idproduct, numofprod): 
        dict[idproduct] = numofprod
        manager.add(dict)

    def purchase():
        manager.executeAll()
    
