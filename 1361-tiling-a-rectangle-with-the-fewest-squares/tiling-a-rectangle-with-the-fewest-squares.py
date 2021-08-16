class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        if n > m:
            n, m = m, n
        
        if n == m:
            return 1
        
        self.ans = n * m
        seen = {}

        def dfs(heights, used):
            if used >= self.ans:
                return
            
            state = tuple(heights)
            if state in seen and seen[state] <= used:
                return
            seen[state] = used

            min_h = min(heights)
            if min_h == n:
                self.ans = min(self.ans, used)
                return

            idx = heights.index(min_h)
            end = idx
            while end < m and heights[end] == min_h:
                end += 1
            
            max_size = min(end - idx, n - min_h)

            for size in range(max_size, 0, -1):
                new_heights = list(heights)
                for j in range(idx, idx + size):
                    new_heights[j] += size
                dfs(new_heights, used + 1)

        dfs([0] * m, 0)
        return self.ans
