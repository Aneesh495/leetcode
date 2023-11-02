
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        # We need the smallest base b >= 2 such that n = 1 + b + b^2 + ... + b^k for some k >= 1
        # Let N be the integer value of n
        N = int(n)

        # Helper that computes the geometric sum 1 + b + ... + b^k
        # Stops early if the value exceeds limit to avoid useless big integer work
        def geom_sum_with_cap(b: int, k: int, limit: int) -> int:
            total = 1
            term = 1
            for _ in range(k):
                term *= b
                if term > limit:
                    return limit + 1
                total += term
                if total > limit:
                    return limit + 1
            return total

        # Maximum k is floor(log2 N) because base is at least 2
        import math
        max_k = int(math.log2(N))

        # Try longer lengths first to ensure the base found is the smallest
        for k in range(max_k, 1, -1):
            # Search b in [2, floor(N ** (1/k))] using binary search with integer math
            # Right bound via integer root by binary lifting to avoid float drift
            # We choose a conservative right bound using pow with float then adjust
            r = int(N ** (1.0 / k))
            while (r + 1) ** k <= N:
                r += 1
            while r ** k > N and r > 2:
                r -= 1

            left, right = 2, r
            while left <= right:
                mid = (left + right) // 2
                s = geom_sum_with_cap(mid, k, N)
                if s == N:
                    return str(mid)
                if s < N:
                    left = mid + 1
                else:
                    right = mid - 1

        # If no k works then the answer is N - 1 because N in base N - 1 is 11
        return str(N - 1)
