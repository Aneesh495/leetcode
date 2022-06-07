class Solution:
    def getSmallestString(self, n, k):
        q, r = divmod(k-n, 25)
        return 'a'*(n-q-(r>0)) + (chr(97+r) if r else '') + 'z'*q