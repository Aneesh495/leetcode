
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atMost(S: int) -> int:
            if S < 0:
                return 0
            res = left = curr = 0
            for right, x in enumerate(nums):
                curr += x
                while curr > S:
                    curr -= nums[left]
                    left += 1
                res += right - left + 1
            return res
        return atMost(goal) - atMost(goal - 1)
