import "sort"

func countMagicalPairs(s string) int64 {
    n := len(s)
    var last, next [26]int
    for i := range last { last[i], next[i] = -1, n }
    following := make([]int, n)
    for i := n-1; i >= 0; i-- {
        c := s[i]-'a'
        following[i] = next[c]
        next[c] = i
    }

    var total int64
    for cut := 0; cut+1 < n; cut++ {
        c := s[cut]-'a'
        last[c] = cut
        next[c] = following[cut]
        leftOrder, rightOrder := last, next
        sort.Ints(leftOrder[:])
        sort.Ints(rightOrder[:])
        for d := 0; d < 26 && leftOrder[25-d] >= 0 && rightOrder[d] < n; d++ {
            leftBoundary, rightBoundary := -1, n
            if d+1 < 26 { leftBoundary, rightBoundary = leftOrder[24-d], rightOrder[d+1] }
            // Consecutive occurrence boundaries delimit choices with exactly d+1 distinct letters.
            total += int64(leftOrder[25-d]-leftBoundary) * int64(rightBoundary-rightOrder[d])
        }
    }
    return total
}