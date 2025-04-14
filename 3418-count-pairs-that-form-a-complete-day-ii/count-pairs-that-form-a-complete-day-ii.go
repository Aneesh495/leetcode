func countCompleteDayPairs(hours []int) int64 {
    var freq [24]int64
    var pairs int64
    for _, hour := range hours {
        remainder := hour % 24
        complement := (24 - remainder) % 24
        pairs += freq[complement]
        freq[remainder]++
    }
    return pairs
}