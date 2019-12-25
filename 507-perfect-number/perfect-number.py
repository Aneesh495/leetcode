
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # A perfect number equals the sum of its positive divisors excluding itself
        if num <= 1:
            return False
        total = 1  # 1 is always a proper divisor for num > 1
        i = 2
        while i * i <= num:
            if num % i == 0:
                total += i
                j = num // i
                if j != i:
                    total += j
            i += 1
        return total == num
