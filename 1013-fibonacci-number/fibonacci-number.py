
class Solution:
    def fib(self, n: int) -> int:
        """
        Compute the n-th Fibonacci number
        F(0) = 0
        F(1) = 1
        For n >= 2
        F(n) = F(n-1) + F(n-2)
        Iterative solution
        Time O(n)
        Space O(1)
        """
        # Handle the two base cases directly
        if n <= 1:
            return n

        # prev2 holds F(i-2) and prev1 holds F(i-1)
        prev2 = 0  # F(0)
        prev1 = 1  # F(1)

        # Loop from i = 2 to n and update the rolling pair
        for _ in range(2, n + 1):
            cur = prev1 + prev2  # F(i) = F(i-1) + F(i-2)
            prev2 = prev1        # shift prev2 to F(i-1)
            prev1 = cur          # shift prev1 to F(i)

        # prev1 now holds F(n)
        return prev1
