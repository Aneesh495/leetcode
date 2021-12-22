class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        low, high = deque(), deque()
        left = best = 0
        for right, x in enumerate(nums):
            while low and nums[low[-1]] > x: low.pop()
            while high and nums[high[-1]] < x: high.pop()
            low.append(right)
            high.append(right)
            while nums[high[0]] - nums[low[0]] > limit:
                if low[0] == left: low.popleft()
                if high[0] == left: high.popleft()
                left += 1
            best = max(best, right-left+1)
        return best