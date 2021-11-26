class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counts = [0] * 501
        for value in arr:
            counts[value] += 1
        for value in range(500, 0, -1):
            if counts[value] == value:
                return value
        return -1