func countValidPrefixes(s string) int {
    answer, difference := 0,0
    for _, letter := range s {
        if letter == '1' { difference++ } else { difference-- }
        // An alternating arrangement is possible exactly when the counts differ by at most one.
        if difference >= -1 && difference <= 1 { answer++ }
    }
    return answer
}