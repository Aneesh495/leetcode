
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        # Sort so divisibility implies a nondecreasing order
        nums.sort()
        
        n = len(nums)
        # dp[i] stores length of the best divisible subset that ends at i
        dp = [1] * n
        # prev[i] stores the previous index used to build the subset that ends at i
        prev = [-1] * n
        
        best_len = 0
        best_end = 0
        
        # Classic longest divisible subset using O(n^2) dynamic programming
        for i in range(n):
            for j in range(i):
                # Since nums is sorted only need to check nums[i] % nums[j] == 0
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i
        
        # Reconstruct the subset by walking prev pointers
        res = []
        k = best_end
        while k != -1:
            res.append(nums[k])
            k = prev[k]
        
        # The reconstruction walks backward so reverse to restore ascending order
        res.reverse()
        return res
