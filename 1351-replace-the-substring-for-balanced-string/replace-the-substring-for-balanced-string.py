from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        target = n // 4
        count = Counter(s)
        
        if all(count[ch] == target for ch in "QWER"):
            return 0
        
        ans = n
        left = 0
        
        for right, ch in enumerate(s):
            count[ch] -= 1
            
            while left < n and all(count[c] <= target for c in "QWER"):
                ans = min(ans, right - left + 1)
                count[s[left]] += 1
                left += 1
        
        return ans
