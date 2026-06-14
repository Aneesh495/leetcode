func countStableSubsequences(nums []int) int {
    const mod = 1000000007
    // ends[p][0] and ends[p][1] count runs of one and two ending values of parity p.
    ends := [2][2]int{}
    for _, value := range nums {
        p := value & 1
        other := p ^ 1
        ends[p][1] = (ends[p][1] + ends[p][0]) % mod
        ends[p][0] = (ends[p][0] + 1 + ends[other][0] + ends[other][1]) % mod
    }
    return (ends[0][0] + ends[0][1] + ends[1][0] + ends[1][1]) % mod
}