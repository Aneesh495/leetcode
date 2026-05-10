func countValidSubsets(parent []int, nums []int, k int) int {
    const mod int64 = 1000000007
    size := len(nums)
    skipped, taken := make([][]int64,size), make([][]int64,size)
    for i, value := range nums {
        skipped[i], taken[i] = make([]int64,k), make([]int64,k)
        skipped[i][0] = 1
        taken[i][value%k] = 1
    }
    for node := size-1; node > 0; node-- {
        p := parent[node]
        combinedSkip, combinedTake := make([]int64,k), make([]int64,k)
        for a := 0; a < k; a++ {
            if skipped[p][a] == 0 && taken[p][a] == 0 { continue }
            for b := 0; b < k; b++ {
                if skipped[node][b] == 0 && taken[node][b] == 0 { continue }
                target := (a+b)%k
                // A selected parent can be combined only with an unselected child.
                combinedSkip[target] = (combinedSkip[target]+skipped[p][a]*(skipped[node][b]+taken[node][b]))%mod
                combinedTake[target] = (combinedTake[target]+taken[p][a]*skipped[node][b])%mod
            }
        }
        skipped[p], taken[p] = combinedSkip, combinedTake
    }
    return int((skipped[0][0]+taken[0][0]+mod-1)%mod)
}