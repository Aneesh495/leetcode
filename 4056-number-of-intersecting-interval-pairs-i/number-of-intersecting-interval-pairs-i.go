func countIntersectingIntervals(intervals [][]int) int {
    answer := 0
    for i, first := range intervals {
        for _, second := range intervals[i+1:] {
            // Closed intervals intersect unless one finishes before the other begins.
            if first[0] <= second[1] && second[0] <= first[1] { answer++ }
        }
    }
    return answer
}