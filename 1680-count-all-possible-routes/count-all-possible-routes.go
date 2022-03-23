func countRoutes(locations []int, start int, finish int, fuel int) int {
    const mod = 1000000007
    n := len(locations)
    memo := make([][]int, n)
    for i := range memo {
        memo[i] = make([]int, fuel+1)
        for j := range memo[i] { memo[i][j] = -1 }
    }
    var dfs func(int, int) int
    dfs = func(city, left int) int {
        if memo[city][left] != -1 { return memo[city][left] }
        ways := 0
        if city == finish { ways = 1 }
        for next := 0; next < n; next++ {
            if next == city { continue }
            cost := locations[city] - locations[next]
            if cost < 0 { cost = -cost }
            if cost <= left { ways = (ways + dfs(next, left-cost)) % mod }
        }
        memo[city][left] = ways
        return ways
    }
    return dfs(start, fuel)
}