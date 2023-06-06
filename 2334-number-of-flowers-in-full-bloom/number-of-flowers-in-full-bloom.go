import "sort"

func fullBloomFlowers(flowers [][]int, people []int) []int {
    starts := make([]int, len(flowers))
    ends := make([]int, len(flowers))
    for i, flower := range flowers {
        starts[i] = flower[0]
        ends[i] = flower[1]
    }
    sort.Ints(starts)
    sort.Ints(ends)

    answer := make([]int, len(people))
    for i, time := range people {
        started := sort.SearchInts(starts, time+1)
        ended := sort.SearchInts(ends, time)
        answer[i] = started - ended
    }
    return answer
}