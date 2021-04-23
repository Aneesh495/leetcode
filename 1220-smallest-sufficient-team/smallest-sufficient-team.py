class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill = {s: i for i, s in enumerate(req_skills)}
        dp = {0: []}
        for i, person in enumerate(people):
            mask = 0
            for s in person:
                mask |= 1 << skill[s]
            for old, team in list(dp.items()):
                new = old | mask
                if new not in dp or len(team) + 1 < len(dp[new]):
                    dp[new] = team + [i]
        return dp[(1 << len(req_skills)) - 1]