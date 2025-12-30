class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        boundaries = {0, n}
        for left, right, _ in queries:
            boundaries.add(left)
            boundaries.add(right + 1)
        points = sorted(boundaries)
        answer = 0

        for index in range(len(points) - 1):
            left, end = points[index], points[index + 1]
            targets = set(nums[left:end])
            required = 0
            for value in targets:
                required |= 1 << value
            if required == 1:
                continue

            maximum = max(targets)
            limit_mask = (1 << (maximum + 1)) - 1
            reachable = 1
            needed = None
            for count, (ql, qr, value) in enumerate(queries, 1):
                if ql <= left <= qr:
                    reachable = (reachable | (reachable << value)) & limit_mask
                    if reachable & required == required:
                        needed = count
                        break
            if needed is None:
                return -1
            answer = max(answer, needed)
        return answer