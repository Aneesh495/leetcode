class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        total = sum(nums)
        prefix = 0
        best = float('inf')
        answer = 0
        n = len(nums)
        for i, value in enumerate(nums):
            prefix += value
            left_avg = prefix // (i + 1)
            right_count = n - i - 1
            right_avg = (total - prefix) // right_count if right_count else 0
            difference = abs(left_avg - right_avg)
            if difference < best:
                best = difference
                answer = i
        return answer