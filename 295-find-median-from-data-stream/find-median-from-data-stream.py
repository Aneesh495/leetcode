import heapq

class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if not self.lower or num <= -self.lower[0]:
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)
        if len(self.lower) > len(self.upper) + 1:
            largest_lower = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, largest_lower)
        elif len(self.upper) > len(self.lower):
            smallest_upper = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -smallest_upper)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return float(-self.lower[0])
        return (-self.lower[0] + self.upper[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()