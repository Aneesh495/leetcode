class Solution:
    def waysToMakeFair(self, nums):
        right = [sum(nums[::2]), sum(nums[1::2])]
        left = [0,0]
        ans = 0
        for i, x in enumerate(nums):
            p = i%2
            right[p] -= x
            ans += left[0]+right[1] == left[1]+right[0]
            left[p] += x
        return ans