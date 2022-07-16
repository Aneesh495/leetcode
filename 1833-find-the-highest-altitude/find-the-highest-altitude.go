func largestAltitude(gain []int) int {
 cur, best := 0, 0
 for _, x := range gain { cur += x; if cur > best { best = cur } }
 return best
}