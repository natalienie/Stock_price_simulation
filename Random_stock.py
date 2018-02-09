import random

class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def change(self, other):
        ox = other.x
        oy = other.y
        time_change = self.x - ox
        price_change = self.y - oy
        return price_change
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

class Chart(object):
    def __init__(self):
        self.stocks = {}
    def addStock(self, stock, loc):
        if stock in self.stocks:
            raise ValueError('Duplicate Stock')
        else:
            self.stocks[stock] = loc
    def getLoc(self, stock):
        if stock not in self.stocks:
            raise ValueError('Stock not in chart')
        return self.stocks[stock]
    def stockChange(self, stock):
        if stock not in self.stocks:
            raise ValueError('Stock not in chart')
        time_change, price_change = stock.tick()
        currentLoc = self.stocks[stock]
        self.stocks[stock] = currentLoc.move(time_change, price_change)

class Stock(object):
    def __init__(self, symbol, vol):
        self.symbol = symbol
        self.vol = vol
    def tick(self):
        num = random.gauss(0, self.vol/16)
        return (1, num)
    def __str__(self):
        return 'The symbol of this stock is ' + self.symbol

def walk(c, s, numTicks):
    '''
    c is the chart; s is the stock; numTicks an int>0
    the stock change numTicks times; returns the change in price
    '''
    start = c.getLoc(s)
    for t in range(numTicks):
        c.stockChange(s)
    return start.change(c.getLoc(s))

def simWalks(numTicks, numTrials):
    MicD = Stock('MicD', 0.492)
    origin = Location(0, 392)
    changed = []
    for t in range(numTrials):
        c = Chart()
        c.addStock(MicD, origin)
        changed.append(round(walk(c, MicD, numTicks), 1))
    return changed

def simTest(tickLengths, numTrials):
    for numTicks in tickLengths:
        price = simWalks(numTicks, numTrials)
        print('random simulation of ', numTicks, 'times')
        print(' Max = ', max(price), 'Min = ', min(price))
