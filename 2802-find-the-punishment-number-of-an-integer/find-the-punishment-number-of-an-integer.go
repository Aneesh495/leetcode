import "strconv"

func punishmentNumber(n int) int {
    total := 0
    for value := 1; value <= n; value++ {
        squareText := strconv.Itoa(value * value)
        var canPartition func(int, int) bool
        canPartition = func(index, sum int) bool {
            if index == len(squareText) {
                return sum == value
            }
            part := 0
            for end := index; end < len(squareText); end++ {
                part = part*10 + int(squareText[end]-'0')
                if sum+part > value {
                    break
                }
                if canPartition(end+1, sum+part) {
                    return true
                }
            }
            return false
        }
        if canPartition(0, 0) {
            total += value * value
        }
    }
    return total
}