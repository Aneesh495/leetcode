class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [-100000] * (target + 1)
        dp[0] = 0
        for value in range(1, target+1):
            for c in cost:
                if c <= value:
                    dp[value] = max(dp[value], dp[value-c] + 1)
        if dp[target] < 0: return "0"
        result = []
        for digit in range(9, 0, -1):
            c = cost[digit-1]
            while target >= c and dp[target] == dp[target-c] + 1:
                result.append(str(digit))
                target -= c
        return "".join(result)