func minimumSum(n int, k int) int {
    // Keep the smaller member of each complementary pair below k.
    low := k / 2
    if n < low { low = n }
    countHigh := n-low
    return low*(low+1)/2 + countHigh*(2*k+countHigh-1)/2
}