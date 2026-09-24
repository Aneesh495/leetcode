from collections import Counter

class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        balance = Counter(nums1)
        balance.subtract(nums2)
        if any(amount % 2 for amount in balance.values()):
            return -1
        # Each swap moves one surplus copy from the first array to the second.
        return sum(amount // 2 for amount in balance.values() if amount > 0)