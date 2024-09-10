
class MyCalendarTwo:

    def __init__(self):
        self.books = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for s, e in self.overlaps:
            if max(s, startTime) < min(e, endTime):
                return False
        for s, e in self.books:
            ls = max(s, startTime)
            le = min(e, endTime)
            if ls < le:
                self.overlaps.append((ls, le))
        self.books.append((startTime, endTime))
        return True
