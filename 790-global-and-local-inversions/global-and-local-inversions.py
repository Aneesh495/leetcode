
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return True
        suffix_min = nums[-1]
        for i in range(n - 3, -1, -1):
            suffix_min = min(suffix_min, nums[i + 2])
            if nums[i] > suffix_min:
                return False
        return True
