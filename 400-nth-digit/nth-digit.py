
class Solution:
    def findNthDigit(self, n: int) -> int:
        # Step 1
        # Determine the digit length 'd' of numbers in the block that contains the nth digit
        d = 1                 # current digit length
        count = 9             # how many numbers have 'd' digits
        start = 1             # first number with 'd' digits
        while n > d * count:
            n -= d * count    # skip entire block of d-digit numbers
            d += 1
            count *= 10
            start *= 10

        # Step 2
        # Locate the exact number that contains the nth digit
        index = (n - 1) // d                 # zero-based index among d-digit numbers
        num = start + index                  # the actual number containing the digit

        # Step 3
        # Pick the digit within that number
        digit_index = (n - 1) % d            # position within the number
        return int(str(num)[digit_index])
