class Order:
    def __init__ (self, quantity, price,buy = True):
        self.quantity = quantity
        self.price = price
        self.buy = buy


    def __str__ (self):
        return "merci mathis il me carry, il aura droit à une chouffe à l'ouverture des bars mais faut pas le dire"
    
    def __repr__(self):

    def quantity(self):
        return self.quantity if self.buy else - self.quantity





class Book:
    def __init__(self,name):
        self.name = name
        self.buyList = list()
        self.sellList = list()
        self.orderId = 0

    def newOrderId(self):
        self.orderId+=1
        return self.orderId

    def maxBuy( ):
    


    def minSell( ):



        

    def insertBuy(quantity, price, Id):
        order = Order(quantity, price, True)
        i=0
        while True : 
            if price >= sellList[i].price and quantity > 0: 
                #on execute l'ordre
                if quantity - sellList[i].quantity >=  0 :
                    quantity = quantity - sellList[i].quantity
                    sellList.pop(i)

                else if quantity - sellList[i].quantity < 0:
                    sellList[i].quantity = sellList[i].quantity - quantity
                    quantity = 0
            i= i+1
       if
                
     self.buyList.append(order)
        




    def insertSell(quantity, price, Id):
        order = Order(quantity, price, False)
        self.sellList.append(order)

