from math import lcm

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        unique = []
        for coin in sorted(coins):
            if all(coin % small for small in unique):
                unique.append(coin)
        high = unique[0] * k

        # Combine inclusion-exclusion terms with the same least common multiple.
        terms = {}
        for coin in unique:
            changes = {coin: 1}
            for old, weight in terms.items():
                merged = lcm(old, coin)
                if merged <= high:
                    changes[merged] = changes.get(merged, 0) - weight
            for divisor, weight in changes.items():
                current = terms.get(divisor, 0) + weight
                if current:
                    terms[divisor] = current
                else:
                    terms.pop(divisor, None)

        low = 1
        while low < high:
            mid = (low + high) // 2
            count = sum(weight * (mid // divisor) for divisor, weight in terms.items())
            if count >= k:
                high = mid
            else:
                low = mid + 1
        return low