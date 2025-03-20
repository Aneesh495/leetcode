func scoreOfString(s string) int {
    score := 0
    for i := 1; i < len(s); i++ {
        diff := int(s[i]) - int(s[i-1])
        if diff < 0 {
            diff = -diff
        }
        score += diff
    }
    return score
}