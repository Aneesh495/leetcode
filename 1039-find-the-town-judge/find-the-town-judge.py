
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # score[x] will increase when someone trusts x
        # score[x] will decrease when x trusts someone
        score = [0] * (n + 1)

        for a, b in trust:
            score[a] -= 1
            score[b] += 1

        # the judge is trusted by everyone and trusts nobody
        # that means score[judge] equals n minus 1
        for person in range(1, n + 1):
            if score[person] == n - 1:
                return person
        return -1
