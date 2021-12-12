class Solution:
    def maxScore(self, s: str) -> int:
        ones_right = s.count('1')
        zeros_left = 0
        best = 0
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1
            best = max(best, zeros_left + ones_right)
        return best