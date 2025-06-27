class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        roads = [[i + 1] for i in range(n - 1)] + [[]]
        distance = list(range(n))
        answer = []
        for start, end in queries:
            roads[start].append(end)
            candidate = distance[start] + 1
            if candidate < distance[end]:
                distance[end] = candidate
                # All roads point forward, so one pass propagates each improvement.
                for city in range(end, n):
                    next_distance = distance[city] + 1
                    for neighbor in roads[city]:
                        if next_distance < distance[neighbor]:
                            distance[neighbor] = next_distance
            answer.append(distance[-1])
        return answer