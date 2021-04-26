from abc import ABCMeta, abstractmethod

# abstract base class (abc)
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class StockTrade():
    def buy(self):
        print('buy stocks')
    def sell(self):
        print('sell stocks')

class Agent():
    def __init__(self):
        self.__orderQueue = [] # an empty list
    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

# concrete classes
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    def execute(self):
        self.stock.sell()

# immediate code
if __name__ == '__main__':
    # client
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    #invoker
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)