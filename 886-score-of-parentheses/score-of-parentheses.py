
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        bal = 0
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                bal += 1
            else:
                bal -= 1
                if s[i - 1] == '(':
                    ans += 1 << bal
        return ans
