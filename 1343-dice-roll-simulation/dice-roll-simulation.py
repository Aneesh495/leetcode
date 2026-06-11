from typing import List

class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        
        dp = [[0] * 16 for _ in range(6)]
        for i in range(6):
            dp[i][1] = 1
        
        for _ in range(2, n + 1):
            face_sum = [sum(dp[i]) % MOD for i in range(6)]
            total = sum(face_sum) % MOD
            new_dp = [[0] * 16 for _ in range(6)]
            
            for i in range(6):
                new_dp[i][1] = (total - face_sum[i]) % MOD
                for cnt in range(1, rollMax[i]):
                    new_dp[i][cnt + 1] = dp[i][cnt]
            
            dp = new_dp
        
        return sum(sum(row) for row in dp) % MOD
