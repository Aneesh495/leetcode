
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Edge case when amount is zero
        if amount == 0:
            return 0

        # Use bottom up dynamic programming
        # dp[x] holds the fewest coins needed to make sum x
        # Initialize with amount + 1 which is an impossible large count
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        # Build answers for all amounts from 1 to amount
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], dp[a - c] + 1)

        # If dp[amount] was not updated it is impossible
        return -1 if dp[amount] > amount else dp[amount]
