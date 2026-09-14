class Solution:
    def minSkips(self, dist: List[int], speed: int, hoursBefore: int) -> int:
        n = len(dist)
        target = hoursBefore * speed
        infinity = 10**30
        dp = [infinity] * (n + 1)
        dp[0] = 0

        for road_index in range(n - 1):
            next_dp = [infinity]* (n + 1)
            road_time = dist[road_index]
            for skips_used in range(road_index +1):
                current_time = dp[skips_used]
                if current_time == infinity:
                    continue
                arrival_time = current_time + road_time

                rested_time = (
                    (arrival_time + speed - 1) // speed
                ) * speed
                next_dp[skips_used] = min(
                    next_dp[skips_used],
                    rested_time,
                )
                next_dp[skips_used + 1] = min(
                    next_dp[skips_used + 1],
                    arrival_time,
                )
            dp = next_dp
        final_road_time = dist[-1]
        answer = -1

        for skips_used in range(n):
            if dp[skips_used] + final_road_time <= target:
                answer = skips_used
                break
        return answer

