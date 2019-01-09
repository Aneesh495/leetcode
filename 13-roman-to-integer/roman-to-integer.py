class Solution:
    def romanToInt(self, s: str) -> int:
        # Map single roman symbols to values
        val = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

        i = 0
        total = 0
        n = len(s)

        # Walk the string from left to right
        while i < n:
            # Value of current symbol
            v = val[s[i]]

            # If next exists and is larger then use subtractive pair
            if i + 1 < n and v < val[s[i + 1]]:
                total += val[s[i + 1]] - v
                i += 2  # Skip the pair
            else:
                total += v
                i += 1

        return total