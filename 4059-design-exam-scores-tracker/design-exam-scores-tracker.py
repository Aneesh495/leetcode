from bisect import bisect_left, bisect_right


class ExamTracker:
    def __init__(self):
        self.times = []
        self.prefix_scores = [0]

    def record(self, time: int, score: int) -> None:
        # Records arrive in strictly increasing time order.
        self.times.append(time)
        self.prefix_scores.append(self.prefix_scores[-1] + score)

    def totalScore(self, startTime: int, endTime: int) -> int:
        # Find the half-open index range for this inclusive time interval.
        left = bisect_left(self.times, startTime)
        right = bisect_right(self.times, endTime)
        return self.prefix_scores[right] - self.prefix_scores[left]