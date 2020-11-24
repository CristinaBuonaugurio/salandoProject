import databaseFolder

class templateAcquisto:
    
    methodOfPayment = None


    def commitPurchase(cliente, value):
        updateQuantityProduct(value)
        setMethodOfPayment()
        hasCoupon()
        commit(cliente, value.keys(), value.items())


    
    def updateQuantityProduct(value):
        functionModels.updateQuantity(value)
       

    def setMethodOfPayment():
        if methodOfPayment is None:
            methodOfPayment = "CONTANTI" 
            
    def hasCoupon():
        pass

    def commit(cliente, product, numofprod):
        functionModels.buyProducts(cliente, value.keys(), value.items() )
