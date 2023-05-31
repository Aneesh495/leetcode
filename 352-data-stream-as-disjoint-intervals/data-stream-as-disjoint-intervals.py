
from bisect import bisect_left

class SummaryRanges:
    def __init__(self):
        self.intervals = []          # list of [l, r] sorted by l
        self.starts = []             # parallel list of l for bisect

    def addNum(self, value: int) -> None:
        i = bisect_left(self.starts, value)

        # Check if value falls inside previous or next interval
        if i > 0 and self.intervals[i - 1][0] <= value <= self.intervals[i - 1][1]:
            return
        if i < len(self.intervals) and self.intervals[i][0] <= value <= self.intervals[i][1]:
            return

        left_merge = i > 0 and self.intervals[i - 1][1] + 1 >= value
        right_merge = i < len(self.intervals) and self.intervals[i][0] - 1 <= value

        if left_merge and right_merge:
            # Merge three parts: prev, value, next
            new_l = self.intervals[i - 1][0]
            new_r = max(self.intervals[i][1], value, self.intervals[i - 1][1])
            self.intervals[i - 1][1] = new_r = max(new_r, self.intervals[i][1])
            # Remove next and update prev end to next end
            self.intervals[i - 1][1] = self.intervals[i][1]
            del self.intervals[i]
            del self.starts[i]
        elif left_merge:
            # Extend previous interval
            self.intervals[i - 1][1] = max(self.intervals[i - 1][1], value)
        elif right_merge:
            # Extend next interval to include value on the left
            self.intervals[i][0] = min(self.intervals[i][0], value)
            self.starts[i] = self.intervals[i][0]
        else:
            # Insert new singleton interval
            self.intervals.insert(i, [value, value])
            self.starts.insert(i, value)

    def getIntervals(self) -> list[list[int]]:
        return [iv[:] for iv in self.intervals]
