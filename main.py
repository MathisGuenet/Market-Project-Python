from book import *

def main():
    book = Book("TEST")
    book.insertBuy(10, 10.0)
    book.insertSell(120, 12.0)
    book.insertBuy(5, 10.0)
    book.insertBuy(2, 11.0)
    book.insertSell(1, 10.0)
    book.insertSell(10, 10.0)
    
if __name__ == "__main__":
    main()

