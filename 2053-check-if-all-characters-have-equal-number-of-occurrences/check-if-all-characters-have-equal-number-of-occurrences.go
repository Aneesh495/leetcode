func areOccurrencesEqual(s string) bool {
    freq := make([]int, 26)
    for _, ch := range s {
        freq[ch-'a']++
    }
    target := 0
    for _, count := range freq {
        if count == 0 {
            continue
        }
        if target == 0 {
            target = count
        } else if count != target {
            return false
        }
    }
    return true
}