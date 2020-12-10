class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        bits = max(nums).bit_length()
        size = 1 << bits
        pairs = [0] * size
        for x in nums:
            for y in nums:
                pairs[x & y] += 1
        for bit in range(bits):
            step = 1 << bit
            for mask in range(size):
                if mask & step:
                    pairs[mask] += pairs[mask ^ step]
        full = size - 1
        return sum(pairs[full ^ x] for x in nums)