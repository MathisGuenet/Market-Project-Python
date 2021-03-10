class Order:
    def __init__ (self, quantity, price,buy = True):
        self.quantity = quantity
        self.price = price
        self.buy = buy

    def newOrderId(self):
        self.orderId+=1
        return self.orderId


    def __str__ (self):
        return "merci mathis il me carry, il aura droit à une chouffe à l'ouverture des bars mais faut pas le dire"

    def __eq__(self, other):
        return other and self.quantity == other.quantity and self.price == other.price
    
    def __lt__(self, other):  #self < other
        return self.price < other.price

    def quantity(self):
        return self.quantity if self.buy else - self.quantity





class Book:
    def __init__(self,name):
        self.name = name
        self.buyList = list()
        self.sellList = list()
        
    def insertBuy(self, quantity, price):
        order = Order(quantity, price, True)
        i=0
        while True :
            if not self.sellList :
                self.buyList.append(order)
            elif price >= self.sellList[i].price and quantity > 0: 
                #on execute l'ordre
                if quantity - self.sellList[i].quantity >=  0 :
                    quantity = quantity - self.sellList[i].quantity
                    self.sellList.pop(i)

                elif quantity - sellList[i].quantity < 0:
                    sellList[i].quantity = sellList[i].quantity - quantity
                    quantity = 0

            else :
                self.buyList.append(order)
            i= i+1

    def sortBuyList(self):
        for i in range(len(self.buyList)):
            if buyList[i + 1].price < buyList[i].price:
                a = buyList[i]
                buyList[i] = buyList[i + 1]
                buyList[i + 1] = a

book = Book("TEST")
book.insertBuy(10, 10.0)
