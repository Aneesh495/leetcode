func minCost(grid [][]int, k int) int {
    rows, cols := len(grid), len(grid[0])
    size := rows*cols
    const infinity = 1000000000
    var prev, current [4][]int
    for d := 0; d < 4; d++ {
        prev[d] = make([]int, size)
        current[d] = make([]int, size)
    }
    dr := [4]int{1,-1,0,0}
    dc := [4]int{0,0,1,-1}
    answer := infinity
    for turns := 0; turns <= k; turns++ {
        for d := 0; d < 4; d++ {
            cost := current[d]
            for i := range cost { cost[i] = infinity }
            if turns == 0 { cost[0] = grid[0][0] }
            // In one direction, sweeping along the movement order resolves all straight moves.
            for ri := 0; ri < rows; ri++ {
                r := ri
                if dr[d] < 0 { r = rows-1-ri }
                for ci := 0; ci < cols; ci++ {
                    c := ci
                    if dc[d] < 0 { c = cols-1-ci }
                    pr,pc := r-dr[d],c-dc[d]
                    if pr < 0 || pr >= rows || pc < 0 || pc >= cols { continue }
                    before := pr*cols + pc
                    best := cost[before]
                    if turns > 0 {
                        for old := 0; old < 4; old++ {
                            if old != d && prev[old][before] < best { best = prev[old][before] }
                        }
                    }
                    here := r*cols+c
                    if best+grid[r][c] < cost[here] { cost[here] = best+grid[r][c] }
                }
            }
            if cost[size-1] < answer { answer = cost[size-1] }
        }
        prev,current = current,prev
    }
    if answer == infinity { return -1 }
    return answer
}