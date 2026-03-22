func maxScore(grid [][]int) int {
    rows, cols := len(grid), len(grid[0])
    best := -1000000000
    for r := 0; r < rows; r++ {
        previous := grid[r][0]
        for c := 1; c < cols; c++ {
            extend := previous + grid[r][c]
            if extend > best { best = extend }
            previous = extend
            if grid[r][c] > previous { previous = grid[r][c] }
        }
    }
    for c := 0; c < cols; c++ {
        previous := grid[0][c]
        for r := 1; r < rows; r++ {
            extend := previous + grid[r][c]
            if extend > best { best = extend }
            previous = extend
            if grid[r][c] > previous { previous = grid[r][c] }
        }
    }
    // Shared cells form one row or column segment. A one-cell crossing needs four neighbors.
    for r := 1; r+1 < rows; r++ {
        for c := 1; c+1 < cols; c++ {
            if grid[r][c] > best { best = grid[r][c] }
        }
    }
    return best
}