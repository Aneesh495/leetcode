func maxDifference(nums []int) int64 {
    var next, afterNext int64
    for i := len(nums)-1; i >= 0; i-- {
        first := int64(nums[i])
        one := first + next
        if first%3 == 0 { one = first - next }
        best := one
        if i+1 < len(nums) {
            sum := first + int64(nums[i+1])
            two := sum + afterNext
            // On a turn switch the following advantage belongs to the opponent.
            if sum%3 == 0 { two = sum - afterNext }
            if two > best { best = two }
        }
        afterNext, next = next, best
    }
    return next
}