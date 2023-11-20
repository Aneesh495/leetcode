import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        ordered = sorted((value, index) for index, value in enumerate(queries))
        visited = [[False] * cols for _ in range(rows)]
        visited[0][0] = True
        frontier = [(grid[0][0], 0, 0)]
        answer = [0] * len(queries)
        reachable = 0
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

        for threshold, index in ordered:
            while frontier and frontier[0][0] < threshold:
                _, r, c = heapq.heappop(frontier)
                reachable += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(frontier, (grid[nr][nc], nr, nc))
            answer[index] = reachable
        return answer