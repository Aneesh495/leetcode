func repeatedStringMatch(a string, b string, x int, y int) bool {
    totalA := int64(len(a)) * int64(x)
    totalB := int64(len(b)) * int64(y)
    if totalB > totalA { return false }

    p, q := len(a), len(b)
    for q != 0 { p, q = q, p%q }
    jointPeriod := len(a) / p * len(b)
    toCompare := jointPeriod
    if totalB < int64(toCompare) { toCompare = int(totalB) }

    // Shifts repeat modulo len(a), and the pair of character streams repeats each joint period.
    for shift := 0; shift < len(a) && int64(shift)+totalB <= totalA; shift++ {
        equal := true
        for j := 0; j < toCompare; j++ {
            if a[(shift+j)%len(a)] != b[j%len(b)] { equal = false; break }
        }
        if equal { return true }
    }
    return false
}