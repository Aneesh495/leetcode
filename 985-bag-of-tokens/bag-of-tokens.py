
from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Greedy two pointers
        # Spend smallest token for score when we can
        # If we cannot and we have score then trade one score to gain power using the largest token
        tokens.sort()
        i = 0
        j = len(tokens) - 1
        score = 0
        best = 0

        while i <= j:
            if power >= tokens[i]:
                power -= tokens[i]
                i += 1
                score += 1
                if score > best:
                    best = score
            elif score > 0 and i < j:
                power += tokens[j]
                j -= 1
                score -= 1
            else:
                break

        return best
