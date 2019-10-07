
class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        Greedy bit logic
        Even n -> halve
        Odd n -> choose +1 or -1 to create more trailing zeros
        Special case 3 prefers -1 to avoid overflow like growth
        """
        steps = 0
        while n != 1:
            if n & 1 == 0:
                # Even number so divide by 2
                n >>= 1
            else:
                # Odd number so decide whether to add 1 or subtract 1
                # If n is 3 or ends with binary 01 then subtract 1
                # Else add 1 to get more zeros after halving
                if n == 3 or (n & 3) == 1:
                    n -= 1
                else:
                    n += 1
            steps += 1
        return steps
