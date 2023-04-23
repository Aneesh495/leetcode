
from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # Build the maximum subsequence of length t from a single array
        # Use a monotonic stack and greedily drop smaller digits while we can
        def pick_max(nums: List[int], t: int) -> List[int]:
            drop = len(nums) - t
            stack: List[int] = []
            for d in nums:
                while drop and stack and stack[-1] < d:
                    stack.pop()
                    drop -= 1
                stack.append(d)
            # Keep only the first t digits
            return stack[:t]

        # Merge two subsequences into the largest possible number
        # At each step pick from the sequence that is lexicographically larger ahead
        def merge(a: List[int], b: List[int]) -> List[int]:
            res: List[int] = []
            i = j = 0
            while i < len(a) or j < len(b):
                # Python supports lexicographic compare of lists
                # Compare the remaining tails to decide which head to take
                if a[i:] > b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            return res

        m, n = len(nums1), len(nums2)
        best: List[int] = []

        # Choose i digits from nums1 and k - i from nums2
        start = max(0, k - n)
        end = min(k, m)
        for i in range(start, end + 1):
            left = pick_max(nums1, i)
            right = pick_max(nums2, k - i)
            cand = merge(left, right)
            if cand > best:
                best = cand
        return best
