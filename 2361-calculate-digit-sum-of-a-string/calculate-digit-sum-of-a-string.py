class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            # Build all groups from the same round before replacing the string.
            groups = [str(sum(map(int, s[i:i + k]))) for i in range(0, len(s), k)]
            s = ''.join(groups)
        return s