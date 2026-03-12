
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold means we currently hold a stock
        # sold means we sold today so tomorrow is cooldown
        # rest means we do not hold and are not in cooldown
        hold = float("-inf")
        sold = float("-inf")
        rest = 0

        for p in prices:
            prev_sold = sold
            sold = hold + p                 # sell today from a hold state
            hold = max(hold, rest - p)      # buy today from a rest state or keep holding
            rest = max(rest, prev_sold)     # stay resting or come from yesterday sold

        return max(sold, rest)
