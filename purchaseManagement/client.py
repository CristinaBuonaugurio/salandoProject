from purchaseManagement import purchase
from databaseFolder import functionModels
class currentUser:

    def __init__(self, idmail):
        self.idmail = idmail
        self.templateacquisto = purchase.templateAcquisto()
        self.manager = purchase.cartManager(templateAcquisto=self.templateacquisto, cliente=self.idmail)

    def getCarts(self):
        return self.manager.getCarts()  

    def addProduct(self, idproduct, numofprod, name): 
        dict = {}
        dict['id'] = idproduct
        dict['numofprod'] = numofprod
        dict['name'] = name
        self.manager.add(value=dict)

    def definitivepurchase(self) -> None:
        self.manager.executeAll()

    def removeProduct(self, idproduct):
        self.manager.remove(idproduct)
    
    def emptyProducts(self): 
        self.manager.removeAll()

    def getMyProfile(self): 
        data = functionModels.getUser(self.idmail)
        data['coupon'] = functionModels.countCoupon(self.idmail)
        return data
