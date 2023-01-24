class Solution:
    def maxProduct(self, s: str) -> int:
        full = (1 << len(s)) - 1
        longest = [0] * (full + 1)

        # Compute the longest palindrome using only the positions in each mask.
        for mask in range(1, full + 1):
            left = mask & -mask
            right = 1 << (mask.bit_length() - 1)
            if left == right:
                longest[mask] = 1
            elif s[left.bit_length() - 1] == s[right.bit_length() - 1]:
                longest[mask] = 2 + longest[mask ^ left ^ right]
            else:
                longest[mask] = max(longest[mask ^ left], longest[mask ^ right])

        # A mask and its complement reserve disjoint indices for the two subsequences.
        return max(longest[mask] * longest[full ^ mask] for mask in range(1, full))