func maximumLength(s string) int {
    lengths := [26][3]int{}
    for left := 0; left < len(s); {
        right := left+1
        for right < len(s) && s[right] == s[left] { right++ }
        row := &lengths[s[left]-'a']
        length := right-left
        for rank := 0; rank < 3; rank++ {
            if length > row[rank] { length, row[rank] = row[rank], length }
        }
        left = right
    }
    answer := -1
    for _, top := range lengths {
        // Three occurrences come from one run, two runs, or three runs.
        twoRuns := top[0]-1
        if top[1] < twoRuns { twoRuns = top[1] }
        for _, length := range []int{top[0]-2, twoRuns, top[2]} {
            if length > 0 && length > answer { answer = length }
        }
    }
    return answer
}