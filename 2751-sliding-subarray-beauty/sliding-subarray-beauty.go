func getSubarrayBeauty(nums []int, k int, x int) []int {
    freq := [101]int{}
    answer := make([]int, len(nums)-k+1)
    for i, value := range nums {
        freq[value+50]++
        if i >= k {
            freq[nums[i-k]+50]--
        }
        if i >= k-1 {
            remaining := x
            for value := -50; value < 0; value++ {
                remaining -= freq[value+50]
                if remaining <= 0 {
                    answer[i-k+1] = value
                    break
                }
            }
        }
    }
    return answer
}