class Order:
    id = 0

    def __init__ (self, quantity, price,buy = True):
        self.quantity = quantity
        self.price = price
        self.buy = buy
        self.ID = Order.id
        Order.id += 1

    def __repr__ (self):
        return "Order(%s, %s, %s)" % (self.quantity, self.price, self.ID)

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

    def __str__(self):
        for i in range(len(book)):
            print(repr(book[i]))

    def insertBuy(self, quantity, price):
        order = Order(quantity, price, True)
        i=0

        if not self.sellList: #sellList is empty
            self.buyList.append(order)
        else: #sellList is not empty
            self.sortSellList()
            while True :
                if order.price >= self.sellList[i].price and order.quantity > 0 : #if we can execute the order
                    if order.quantity - self.sellList[i].quantity >=  0 :
                        order.quantity = order.quantity - self.sellList[i].quantity
                        self.sellList.pop(i) #delete sell order
                        self.buyList.append(order) #Add buy order
                    else: # order.quantity - self.sellList[i].quantity < 0
                        self.sellList[i].quantity = self.sellList[i].quantity - quantity
                        order.quantity = 0
                else : #we can't execute the order and we just add it to the book
                    self.buyList.append(order)
                i= i+1
    
    def insertSell(self, quantity, price):
        order = Order(quantity, price, False)
        i = 0

        if not self.buyList: #buyList is empty
            self.sellList.append(order)
        else: #buyList is not empty
            self.sortBuyList()
            while True:
                if order.price <= self.buyList[i].price and order.quantity > 0 :
                    #on execute l'odre
                    if order.quantity - self.buyList[i].quantity >= 0:
                        order.quantity = order.quantity - self.buyList[i].quantity
                        self.buyList.pop(i) #delete buy order
                        self.sellList.append(order) #add sell order in the book
                    else:
                        self.buyList[i] = order.quantity - self.buyList[i].quantity
                        order.quantity = 0
                else : #we can't execute the order and we just add it to the book
                    self.sellList.append(order)
                i = i + 1

    def sortBuyList(self): #We want to sort data in function of price (decreasing) and then id(increasing)
        self.buyList.sort(key=lambda x : x.price)

    def sortSellList(self):
        self.sellList.sort(key=lambda x : x.price, reverse= True)
    
book = Book("TEST")
print(Book)
book.insertBuy(10, 10.0)
print(Book)
book.insertSell(120, 12.0)
book.insertBuy(5, 10.0)
book.insertBuy(2, 11.0)
book.insertSell(1, 10.0)
book.insertSell(10, 10.0)
