func maxSubsequence(nums []int, k int) []int {
    chosen := make([]bool, len(nums))
    for count := 0; count < k; count++ {
        best := -1
        for i, value := range nums {
            if !chosen[i] && (best == -1 || value > nums[best]) {
                best = i
            }
        }
        chosen[best] = true
    }
    answer := make([]int, 0, k)
    for i, value := range nums {
        if chosen[i] {
            answer = append(answer, value)
        }
    }
    return answer
}