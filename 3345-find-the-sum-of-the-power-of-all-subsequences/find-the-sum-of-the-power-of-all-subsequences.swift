class Solution {
    func sumOfPower(_ nums: [Int], _ k: Int) -> Int {
        let mod = 1_000_000_007
        var dp = Array(repeating: 0, count: k + 1)
        dp[0] = 1
        for value in nums {
            for sum in stride(from: k, through: 0, by: -1) {
                var ways = (2 * dp[sum]) % mod
                if sum >= value { ways = (ways + dp[sum - value]) % mod }
                dp[sum] = ways
            }
        }
        return dp[k]
    }
}