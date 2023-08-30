func secondsToRemoveOccurrences(s string) int {
    zeros := 0
    seconds := 0
    for _, ch := range s {
        if ch == '0' {
            zeros++
        } else if zeros > 0 {
            if seconds+1 > zeros {
                seconds++
            } else {
                seconds = zeros
            }
        }
    }
    return seconds
}