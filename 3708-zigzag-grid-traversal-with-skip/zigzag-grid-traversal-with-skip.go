func zigzagTraversal(grid [][]int) []int {
    width := len(grid[0])
    result := make([]int, 0, (len(grid)*width+1)/2)
    for row, values := range grid {
        // Keep global traversal indices that are even, including across row boundaries.
        start := (row * width) % 2
        for offset := start; offset < width; offset += 2 {
            column := offset
            if row%2 == 1 {
                column = width - 1 - offset
            }
            result = append(result, values[column])
        }
    }
    return result
}