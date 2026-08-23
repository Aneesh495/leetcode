func countSuffix(nums []int, target []int) int {
    prefixLimit := 0
    for prefixLimit < len(nums) && nums[prefixLimit] == target[prefixLimit] { prefixLimit++ }
    balance := make([]int, 100001)
    different := 0
    change := func(value, delta int) {
        if balance[value] == 0 { different++ }
        balance[value] += delta
        if balance[value] == 0 { different-- }
    }
    answer := 0
    for i := len(nums)-1; i >= 0; i-- {
        if i+1 < len(nums) && target[i] < target[i+1] { break }
        change(nums[i],1)
        change(target[i],-1)
        // Prefixes match, and this non-increasing suffix uses exactly the original values.
        if i <= prefixLimit && different == 0 { answer++ }
    }
    return answer
}