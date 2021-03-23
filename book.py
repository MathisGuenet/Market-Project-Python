import pandas as pd

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

    def __repr__(self):
        print("---------SellList---------")
        d = {'quantity':[order.quantity for order in self.sellList], 'price':[order.price for order in self.sellList], 'ID':[order.ID for order in self.sellList]}
        df_sell = pd.DataFrame(data = d)
        print(df_sell)
        print("\n---------BuyList----------")
        d = {'quantity':[order.quantity for order in self.buyList], 'price':[order.price for order in self.buyList], 'ID':[order.ID for order in self.buyList]}
        df_buy = pd.DataFrame(data = d)
        print(df_buy)
        res = "\n----------------Next Step----------------\n"
        return res

    def insertBuy(self, quantity, price):
        order = Order(quantity, price, True)
        print("--Insert BUY " + repr(order) + " on " + self.name + "\n")
        i=0
        if not self.sellList: #sellList is empty
            self.buyList.append(order)
        else: #sellList is not empty
            self.sortSellList()
            while True :
                if order.price >= self.sellList[i].price and order.quantity > 0 : #if we can execute the order
                    if order.quantity - self.sellList[i].quantity >=  0 :
                        order.quantity = order.quantity - self.sellList[i].quantity
                        print("Execute " +  str(self.sellList[i].quantity) + " at " + str(self.sellList[i].price))
                        self.sellList.pop(i) #delete sell order
                    else: # order.quantity - self.sellList[i].quantity < 0
                        self.sellList[i].quantity = self.sellList[i].quantity - order.quantity
                        print("Execute " + str(order.quantity) + " at " + str(self.sellList[i].price))
                        order.quantity = 0
                else : #we can't execute the order and we just add it to the book
                    if order.quantity > 0:
                        self.buyList.append(order)
                        self.sortBuyList()
                    break
        print(repr(self))

    
    def insertSell(self, quantity, price):
        order = Order(quantity, price, False)
        print("--Insert SELL " + repr(order) + " on " + self.name + "\n")
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
                        print("Execute " +  str(self.buyList[i].quantity) + " at " + str(self.buyList[i].price))
                        self.buyList.pop(i) #delete buy order
                    else:
                        self.buyList[i].quantity = self.buyList[i].quantity - order.quantity 
                        print("Execute " + str(order.quantity) + " at " + str(self.buyList[i].price))
                        order.quantity = 0
                else : #we can't execute the order and we just add it to the book
                    if order.quantity > 0:
                        self.sellList.append(order)
                        self.sortSellList()
                    break
        print(repr(self))

    def sortBuyList(self): #We want to sort data in function of price (decreasing) and then id(increasing)
        self.buyList.sort(key=lambda x : x.price, reverse= True)

    def sortSellList(self):
        self.sellList.sort(key=lambda x : x.price, reverse= False)

if __name__ == "__main__":
    book = Book("TEST")
    book.insertBuy(10, 10.0)
    book.insertSell(120, 12.0)
    book.insertBuy(5, 10.0)
    book.insertBuy(2, 11.0)
    book.insertSell(1, 10.0)
    book.insertSell(10, 10.0)
