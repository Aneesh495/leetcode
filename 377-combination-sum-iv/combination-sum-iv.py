
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Bottom up DP where dp[t] is the number of ordered sequences that sum to t
        nums.sort()
        dp = [0] * (target + 1)
        dp[0] = 1
        for t in range(1, target + 1):
            for x in nums:
                if x > t:
                    break
                dp[t] += dp[t - x]
        return dp[target]
