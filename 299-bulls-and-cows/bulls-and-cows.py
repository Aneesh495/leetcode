
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # Count bulls in a single pass and collect non matching digits
        bulls = 0
        cnt_secret = [0] * 10  # counts of digits 0 to 9 for secret where not a bull
        cnt_guess = [0] * 10   # counts of digits 0 to 9 for guess where not a bull

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cnt_secret[ord(s) - 48] += 1
                cnt_guess[ord(g) - 48] += 1

        # Cows are the sum of the minimum counts for each digit
        cows = sum(min(cnt_secret[d], cnt_guess[d]) for d in range(10))

        return f"{bulls}A{cows}B"
