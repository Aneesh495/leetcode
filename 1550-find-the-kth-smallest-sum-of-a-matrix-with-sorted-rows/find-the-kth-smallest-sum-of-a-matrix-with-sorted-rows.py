class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        import heapq
        sums = [0]
        for row in mat:
            heap = [(x + row[0], i, 0) for i, x in enumerate(sums)]
            heapq.heapify(heap)
            merged = []
            while heap and len(merged) < k:
                value, i, j = heapq.heappop(heap)
                merged.append(value)
                if j + 1 < len(row):
                    heapq.heappush(heap, (sums[i] + row[j+1], i, j+1))
            sums = merged
        return sums[k-1]