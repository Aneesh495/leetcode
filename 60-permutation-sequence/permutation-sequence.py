class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        available = list(range(1, n + 1))
        result = []
        block_size = 1

        for value in range(2, n):
            block_size *= value
        k -= 1
        
        for remaining in range(n, 0, -1):
            index = k // block_size
            k %= block_size
            chosen = available.pop(index)
            result.append(str(chosen))
            if remaining > 1:
                block_size //= remaining - 1
        return "".join(result)