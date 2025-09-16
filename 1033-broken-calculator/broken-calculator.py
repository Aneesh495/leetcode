
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        """
        Greedy from target back to start.
        If target is even then the best reverse step is divide by two.
        If target is odd then the best reverse step is add one to make it even.
        Once target is not greater than startValue the only option is subtract.
        Time O(log target). Space O(1).
        """
        if target <= startValue:
            return startValue - target

        ops = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            ops += 1

        # Now target <= startValue, need the remaining decrements
        return ops + (startValue - target)
