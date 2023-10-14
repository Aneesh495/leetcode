
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        """
        LeetCode 467
        Count unique non-empty substrings of s that appear in the infinite wraparound string
        "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz..."
        Idea:
          Track, for each letter 'a'..'z', the maximum length of a valid wraparound substring
          that ends with that letter. Any shorter length ending at the same letter is included,
          so summing these maxima gives the total unique substrings.
        Time O(n)  Space O(1)
        """
        if not s:
            return 0

        # max_len_end[c] stores the longest valid length of a substring ending with chr(c + 'a')
        max_len_end = [0] * 26

        # current run length of consecutive wraparound characters
        run = 0

        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                run += 1
            else:
                run = 1

            idx = ord(ch) - ord('a')
            # Only keep the best for each ending character
            if run > max_len_end[idx]:
                max_len_end[idx] = run

        return sum(max_len_end)
