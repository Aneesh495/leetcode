
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # XOR all character codes in s and t
        # Pairs cancel out and the added char remains
        x = 0
        for ch in s:
            x ^= ord(ch)
        for ch in t:
            x ^= ord(ch)
        return chr(x)
