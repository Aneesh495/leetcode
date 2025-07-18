import "sort"

type rookCandidate struct {
    col int
    value int
}

func maximumValueSum(board [][]int) int64 {
    rows, cols := len(board), len(board[0])
    top := make([][]rookCandidate, rows)
    for r := 0; r < rows; r++ {
        cells := make([]rookCandidate, cols)
        for c := 0; c < cols; c++ {
            cells[c] = rookCandidate{col: c, value: board[r][c]}
        }
        sort.Slice(cells, func(i, j int) bool { return cells[i].value > cells[j].value })
        top[r] = cells[:3]
    }

    best := int64(-1 << 63)
    for r1 := 0; r1 < rows; r1++ {
        for r2 := r1 + 1; r2 < rows; r2++ {
            for r3 := r2 + 1; r3 < rows; r3++ {
                for _, a := range top[r1] {
                    for _, b := range top[r2] {
                        if a.col == b.col { continue }
                        for _, c := range top[r3] {
                            if c.col == a.col || c.col == b.col { continue }
                            sum := int64(a.value) + int64(b.value) + int64(c.value)
                            if sum > best { best = sum }
                        }
                    }
                }
            }
        }
    }
    return best
}