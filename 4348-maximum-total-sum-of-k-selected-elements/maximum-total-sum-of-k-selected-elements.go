import "sort"

func maxSum(nums []int, k int, mul int) int64 {
    sort.Ints(nums)
    var total int64
    for i := 0; i < k; i++ {
        weight := mul-i
        if weight < 1 { weight = 1 }
        // Equal or larger weights belong to the larger selected values.
        total += int64(nums[len(nums)-1-i])*int64(weight)
    }
    return total
}