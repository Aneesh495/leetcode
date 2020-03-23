
class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        steps, d = 0, 2
        while d * d <= n:
            while n % d == 0:
                steps += d
                n //= d
            d += 1
        if n > 1:
            steps += n
        return steps
