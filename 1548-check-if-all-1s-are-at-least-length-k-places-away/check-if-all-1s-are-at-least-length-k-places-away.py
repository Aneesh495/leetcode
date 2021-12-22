class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        previous = -k-1
        for i, x in enumerate(nums):
            if x:
                if i - previous <= k: return False
                previous = i
        return True