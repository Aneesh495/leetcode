
class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        """
        Determine if it's possible to measure exactly `target` liters using two jugs
        with capacities `x` and `y`. Operations allowed are fill empty and pour.

        Key facts
        • If target is 0 then it's trivially possible
        • You can never have more than x + y total water
        • Bézout's identity applies. You can measure any multiple of gcd(x, y)
          up to x + y
        """
        from math import gcd

        # Trivial success
        if target == 0:
            return True

        # Total water limit
        if target > x + y:
            return False

        # If both jugs are zero then only target 0 is possible
        if x == 0 and y == 0:
            return False  # target cannot be > 0 here due to prior check

        # If one jug is zero then you can only measure target if it equals the other jug
        if x == 0:
            return target == y
        if y == 0:
            return target == x

        # Core Bézout condition
        return target % gcd(x, y) == 0
