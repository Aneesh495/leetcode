import "math/bits"

func calculateScore(a int, b int) int {
    first := bits.OnesCount(uint(a))
    second := bits.OnesCount(uint(b))
    if first >= second { return first * second }
    return second / first
}