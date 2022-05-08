class Solution:
    def bestTeamScore(self, scores: list[int], ages: list[int]) -> int:
        players = sorted(zip(ages, scores))
        dp = [0] * len(players)
        answer = 0
        for i, (_, score) in enumerate(players):
            best_previous = 0
            for j in range(i):
                if players[j][1] <= score:
                    best_previous = max(best_previous, dp[j])
            dp[i] = best_previous + score
            answer = max(answer, dp[i])
        return answer