import heapq

class StockPrice:

    def __init__(self):
        self.prices = {}
        self.latest_heap = []
        self.maximum_heap = []
        self.minimum_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.prices[timestamp] = price
        heapq.heappush(self.latest_heap, -timestamp)
        heapq.heappush(self.maximum_heap, (-price, timestamp))
        heapq.heappush(self.minimum_heap, (price, timestamp))

    def current(self) -> int:
        latest_timestamp = -self.latest_heap[0]
        return self.prices[latest_timestamp]

    def maximum(self) -> int:
        while True:
            negative_price, timestamp = self.maximum_heap[0]
            if self.prices[timestamp] == -negative_price:
                return -negative_price
            heapq.heappop(self.maximum_heap)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.minimum_heap[0]
            if self.prices[timestamp] == price:
                return price
            heapq.heappop(self.minimum_heap)


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()