
class Solution:
    def countAndSay(self, n: int) -> str:
        """
        Generate the nth term of the count and say sequence.
        Build iteratively from "1" using run length encoding of digits.
        """
        s = "1"                       # term for n = 1
        for _ in range(n - 1):        # build next term n-1 times
            res = []                  # collect pieces for the next term
            i = 0
            while i < len(s):
                j = i
                # advance j while the same digit repeats
                while j < len(s) and s[j] == s[i]:
                    j += 1
                count = j - i         # number of repeats
                res.append(str(count))# say the count
                res.append(s[i])      # then the digit
                i = j                 # move to the next new digit run
            s = "".join(res)          # next term ready
        return s