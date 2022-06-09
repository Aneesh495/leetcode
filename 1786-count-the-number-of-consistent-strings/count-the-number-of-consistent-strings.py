class Solution:
    def countConsistentStrings(self, allowed, words):
        chars=set(allowed)
        return sum(set(w)<=chars for w in words)