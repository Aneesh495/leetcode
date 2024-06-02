func lengthOfLongestSubsequence(nums []int, target int) int {
    dp := make([]int, target+1)
    for i := 1; i <= target; i++ {
        dp[i] = -1
    }
    for _, x := range nums {
        for sum := target; sum >= x; sum-- {
            if dp[sum-x] >= 0 && dp[sum-x]+1 > dp[sum] {
                dp[sum] = dp[sum-x] + 1
            }
        }
    }
    return dp[target]
}