
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window that tracks counts of letters in current window
        # max_freq stores the count of the most frequent letter in the window
        counts = [0] * 26
        left = 0
        max_freq = 0
        best = 0

        for right, ch in enumerate(s):
            idx = ord(ch) - 65  # 'A' to 'Z'
            counts[idx] += 1
            if counts[idx] > max_freq:
                max_freq = counts[idx]

            # If replacements needed exceed k then shrink from the left
            while (right - left + 1) - max_freq > k:
                counts[ord(s[left]) - 65] -= 1
                left += 1

            # Update best window length
            window_len = right - left + 1
            if window_len > best:
                best = window_len

        return best
