
from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        """
        Return all distinct values of x^i + y^j that are <= bound
        Uses multiplicative generation of powers for x and y
        Handles x == 1 or y == 1 to avoid infinite loops
        """
        if bound < 2:
            return []

        ans: set[int] = set()

        xi = 1
        while xi <= bound:
            yj = 1
            while yj <= bound:
                s = xi + yj
                if s <= bound:
                    ans.add(s)
                else:
                    # y^j will only grow so break
                    break

                if y == 1:
                    # further multiples would be same value
                    break
                yj *= y

            if x == 1:
                # further multiples would be same value
                break
            xi *= x

        return sorted(ans)
