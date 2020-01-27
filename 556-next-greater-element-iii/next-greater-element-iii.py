
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        # Convert to a list of characters for in place edits
        digits = list(str(n))

        # Step 1. Find the first index i from the right where digits[i] is smaller than digits[i + 1]
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        if i < 0:
            return -1  # Already the greatest permutation

        # Step 2. Find the smallest digit to the right of i that is greater than digits[i]
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1

        # Step 3. Swap and then reverse the suffix to get the minimal greater number
        digits[i], digits[j] = digits[j], digits[i]
        digits[i + 1:] = reversed(digits[i + 1:])

        # Step 4. Convert back and check 32 bit signed range
        ans = int("".join(digits))
        return ans if ans < 2**31 else -1
