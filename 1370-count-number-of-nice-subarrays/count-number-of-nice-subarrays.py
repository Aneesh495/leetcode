from typing import List
from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        
        odd = 0
        ans = 0
        
        for num in nums:
            odd += num % 2
            ans += count[odd - k]
            count[odd] += 1
        
        return ans
