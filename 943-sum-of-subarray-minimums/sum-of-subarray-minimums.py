
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        stack = []
        ans = 0
        for i in range(len(arr) + 1):
            cur = arr[i] if i < len(arr) else 0
            while stack and (i == len(arr) or arr[stack[-1]] >= cur):
                j = stack.pop()
                k = stack[-1] if stack else -1
                ans = (ans + arr[j] * (j - k) * (i - j)) % MOD
            stack.append(i)
        return ans % MOD
