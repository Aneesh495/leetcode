class Solution:
    def halvesAreAlike(self, s):
        m=len(s)//2; v=set('aeiouAEIOU')
        return sum(c in v for c in s[:m]) == sum(c in v for c in s[m:])