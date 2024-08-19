
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash = 0
        hold = -10**18
        for p in prices:
            prev_cash = cash
            cash = max(cash, hold + p - fee)
            hold = max(hold, prev_cash - p)
        return cash
