func minOperations(nums []int) int {
    maximum := 0
    for _, value := range nums { if value > maximum { maximum = value } }
    smallestPrime := make([]int, maximum+1)
    for prime := 2; prime <= maximum; prime++ {
        if smallestPrime[prime] == 0 {
            smallestPrime[prime] = prime
            if prime <= maximum/prime {
                for multiple := prime*prime; multiple <= maximum; multiple += prime {
                    if smallestPrime[multiple] == 0 { smallestPrime[multiple] = prime }
                }
            }
        }
    }
    operations := 0
    for i := len(nums)-2; i >= 0; i-- {
        if nums[i] > nums[i+1] {
            value := nums[i]
            if smallestPrime[value] == value { return -1 }
            reduced := smallestPrime[value]
            if reduced > nums[i+1] { return -1 }
            nums[i] = reduced
            operations++
        }
    }
    return operations
}