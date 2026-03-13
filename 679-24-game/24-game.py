
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        nums = [float(x) for x in cards]

        def dfs(arr: List[float]) -> bool:
            if len(arr) == 1:
                return abs(arr[0] - 24.0) < EPS

            n = len(arr)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    a, b = arr[i], arr[j]
                    rest = [arr[k] for k in range(n) if k != i and k != j]

                    for val in (a + b, a - b, b - a, a * b):
                        if dfs(rest + [val]):
                            return True
                    if abs(b) > EPS and dfs(rest + [a / b]):
                        return True
                    if abs(a) > EPS and dfs(rest + [b / a]):
                        return True
            return False

        return dfs(nums)
