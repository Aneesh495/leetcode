
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Quick fail if ransomNote is longer than magazine
        if len(ransomNote) > len(magazine):
            return False

        # Count available letters in magazine using a fixed array for 26 lowercase letters
        counts = [0] * 26
        for ch in magazine:
            counts[ord(ch) - 97] += 1

        # Spend letters to build the ransomNote
        for ch in ransomNote:
            i = ord(ch) - 97
            counts[i] -= 1
            if counts[i] < 0:
                return False

        return True
