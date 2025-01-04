
class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        pre = [0]
        for x in nums:
            pre.append(pre[-1] + x)

        def avg(i, j):
            return (pre[j] - pre[i]) / (j - i)

        dp = [0.0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = avg(i, n)

        for p in range(2, k + 1):
            ndp = [0.0] * (n + 1)
            # need at least p elements to make p groups
            for i in range(n - p + 1, -1, -1):
                best = 0.0
                # j is the start of the next group, leave at least p-1 elements
                for j in range(i + 1, n - (p - 1) + 1):
                    val = avg(i, j) + dp[j]
                    if val > best:
                        best = val
                ndp[i] = best
            dp = ndp

        return dp[0]
