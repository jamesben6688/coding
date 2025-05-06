from sortedcontainers.sorteddict import SortedDict


class StockPrice:

    def __init__(self):
        self.stock_price = SortedDict()
        self.mx = 0
        self.mn = float('inf')

    def update(self, timestamp: int, price: int) -> None:
        self.stock_price[timestamp] = price
        self.mx = max(self.mx, price)
        self.mn = min(self.mn, price)

    def current(self) -> int:
        print(self.stock_price.keys()[-1])
        return self.stock_price[self.stock_price.keys()[-1]]

    def maximum(self) -> int:
        return self.mx

    def minimum(self) -> int:
        return self.mn


# Your StockPrice object will be instantiated and called as such:
obj = StockPrice()
ops = ["StockPrice","update","update","current","maximum","update","maximum","update","minimum"]
params = [[],[1,10],[2,5],[],[],[1,3],[],[4,2],[]]
for i in range(1, len(ops)):
    if 'update' in ops[i]:
        obj.update(*params[i])
    elif 'current' in ops[i]:
        print(obj.current())
    elif 'max' in ops[i]:
        print(obj.maximum())
    else:
        print(obj.minimum())
