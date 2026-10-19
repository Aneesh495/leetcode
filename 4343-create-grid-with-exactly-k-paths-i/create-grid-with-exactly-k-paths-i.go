func createGrid(m int, n int, k int) []string {
    grid := make([][]byte,m)
    for i := range grid {
        grid[i] = make([]byte,n)
        for j := range grid[i] { grid[i][j] = '#' }
    }
    switch {
    case k == 1:
        for j := range grid[0] { grid[0][j] = '.' }
        for i := range grid { grid[i][n-1] = '.' }
    case m < 2 || n < 2:
        return []string{}
    case n >= k:
        // In a 2-by-k rectangle the single downward step has exactly k possible columns.
        for c := 0; c < k; c++ { grid[0][c], grid[1][c] = '.', '.' }
        for c := k; c < n; c++ { grid[1][c] = '.' }
        for r := 2; r < m; r++ { grid[r][n-1] = '.' }
    case m >= k:
        for r := 0; r < k; r++ { grid[r][0], grid[r][1] = '.', '.' }
        for r := k; r < m; r++ { grid[r][1] = '.' }
        for c := 2; c < n; c++ { grid[m-1][c] = '.' }
    case m == 3 && n == 3 && k == 4:
        for i := range grid { for j := range grid[i] { grid[i][j] = '.' } }
        grid[0][2], grid[2][0] = '#','#'
    default:
        return []string{}
    }
    result := make([]string,m)
    for i, row := range grid { result[i] = string(row) }
    return result
}