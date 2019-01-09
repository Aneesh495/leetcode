
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Handle empty input
        if not strs:
            return ""
        # The common prefix of the whole set must be a prefix of both
        # the lexicographically smallest and largest strings
        first = min(strs)
        last = max(strs)

        # Compare characters until they differ
        i = 0
        n = min(len(first), len(last))
        while i < n and first[i] == last[i]:
            i += 1

        return first[:i]