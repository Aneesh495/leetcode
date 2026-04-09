from heapq import heappop, heappush

class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        limit = 2 * m * n
        distance = [10 ** 24] * limit
        distance[0] = 1
        heap = [(1, 0)]
        moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while heap:
            cost, state = heappop(heap)
            if cost != distance[state]:
                continue
            cell, phase = divmod(state, 2)
            if cell == m * n - 1:
                return cost
            row, col = divmod(cell, n)
            next_phase = phase ^ 1
            charge = penalty[row][col]
            waiting = 2 * cell + next_phase
            if cost + charge < distance[waiting]:
                distance[waiting] = cost + charge
                heappush(heap, (distance[waiting], waiting))
            for direction, (dr, dc) in enumerate(moves):
                nr, nc = row + dr, col + dc
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                # Any action flips the required direction group for the next move.
                target = 2 * (nr * n + nc) + next_phase
                candidate = cost + (nr + 1) * (nc + 1)
                if direction // 2 != phase:
                    candidate += charge
                if candidate < distance[target]:
                    distance[target] = candidate
                    heappush(heap, (candidate, target))
        return -1