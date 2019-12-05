
class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1 if n == 1 else 1 if n == 2 else 1  # "122"
        s = [1, 2, 2]
        i = 2
        num = 1
        count = 1  # count of 1s within first n
        while len(s) < n:
            times = s[i]
            for _ in range(times):
                s.append(num)
                if len(s) <= n and num == 1:
                    count += 1
            num = 2 if num == 1 else 1
            i += 1
        return count
