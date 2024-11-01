
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_so_far = -1
        for i, v in enumerate(arr):
            max_so_far = max(max_so_far, v)
            if max_so_far == i:
                chunks += 1
        return chunks
