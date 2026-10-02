class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        def through(bound):
            if bound < 0:
                return 0
            low, high = 0, bound
            while low < high:
                mid = (low + high + 1) // 2
                if mid ** k <= bound:
                    low = mid
                else:
                    high = mid - 1
            # Include zero and count each distinct power once.
            return low + 1

        return through(r) - through(l - 1)