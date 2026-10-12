func shadowPairs(nums []int) int64 {
    type group struct { value, count int }
    stack := make([]group, 0, len(nums))
    active := 0
    var total int64
    for _, value := range nums {
        // A smaller arrival permanently blocks each larger prior index.
        for len(stack) > 0 && stack[len(stack)-1].value > value {
            active -= stack[len(stack)-1].count
            stack = stack[:len(stack)-1]
        }
        if len(stack) > 0 && stack[len(stack)-1].value == value {
            last := len(stack)-1
            total += int64(active-stack[last].count)
            stack[last].count++
        } else {
            total += int64(active)
            stack = append(stack, group{value, 1})
        }
        active++
    }
    return total
}