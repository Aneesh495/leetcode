func findMiddleIndex(nums []int) int {
    right := 0
    for _, value := range nums {
        right += value
    }

    left := 0
    for i, value := range nums {
        // Remove the current element before comparing the two sides.
        right -= value
        if left == right {
            return i
        }
        left += value
    }
    return -1
}