func countGoodSubstrings(s string) int {
    count := 0
    for i := 0; i+2 < len(s); i++ {
        if s[i] != s[i+1] && s[i] != s[i+2] && s[i+1] != s[i+2] {
            count++
        }
    }
    return count
}