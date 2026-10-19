func maxValidPairSum(nums []int, k int) int {
    largest := nums[0]
    answer := 0
    for right := k; right < len(nums); right++ {
        // Exactly one more index becomes far enough to pair with right.
        if nums[right-k] > largest { largest = nums[right-k] }
        if nums[right]+largest > answer { answer = nums[right]+largest }
    }
    return answer
}