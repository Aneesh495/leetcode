func maxPartitionsAfterOperations(s string, k int) int {
    n := len(s)
    next := make([]int, n)
    freq := [26]int{}
    right, distinct := 0, 0
    for left := 0; left < n; left++ {
        for right < n {
            c := s[right] - 'a'
            if freq[c] == 0 && distinct == k { break }
            if freq[c] == 0 { distinct++ }
            freq[c]++
            right++
        }
        next[left] = right
        c := s[left] - 'a'
        freq[c]--
        if freq[c] == 0 { distinct-- }
    }
    parts := make([]int, n+1)
    for i := n-1; i >= 0; i-- { parts[i] = 1 + parts[next[i]] }
    starts, before := make([]int, n), make([]int, n)
    done, start := 0, 0
    for start < n {
        end := next[start]
        for i := start; i < end; i++ { starts[i], before[i] = start, done }
        done++
        start = end
    }
    pref := make([][26]int, n+1)
    for i := 0; i < n; i++ { pref[i+1] = pref[i]; pref[i+1][s[i]-'a']++ }
    nextPos := make([][26]int, n+1)
    for c := 0; c < 26; c++ { nextPos[n][c] = n }
    for i := n-1; i >= 0; i-- { nextPos[i] = nextPos[i+1]; nextPos[i][s[i]-'a'] = i }
    type Item struct { pos, ch int }
    order := make([][26]Item, n)
    for i := 0; i < n; i++ {
        for c := 0; c < 26; c++ { order[i][c] = Item{nextPos[i+1][c], c} }
        for j := 1; j < 26; j++ {
            item, p := order[i][j], j-1
            for p >= 0 && order[i][p].pos > item.pos { order[i][p+1] = order[i][p]; p-- }
            order[i][p+1] = item
        }
    }
    answer := parts[0]
    for i := 0; i < n; i++ {
        base, doneBefore := starts[i], before[i]
        if i == base && base > 0 { base = starts[base-1]; doneBefore = before[base] }
        var mask uint32
        distinctBefore := 0
        for c := 0; c < 26; c++ {
            if pref[i][c]-pref[base][c] > 0 { mask |= uint32(1)<<uint(c); distinctBefore++ }
        }
        for ch := 0; ch < 26; ch++ {
            bit := uint32(1)<<uint(ch)
            afterMask, d := mask|bit, distinctBefore
            if mask&bit == 0 { d++ }
            if d <= k {
                need, seen, end := k-d+1, 0, n
                for _, item := range order[i] {
                    if item.pos == n { break }
                    if afterMask&(uint32(1)<<uint(item.ch)) == 0 { seen++; if seen == need { end = item.pos; break } }
                }
                candidate := doneBefore+1+parts[end]
                if candidate > answer { answer = candidate }
            } else {
                seen, end := 0, n
                for _, item := range order[i] {
                    if item.pos == n { break }
                    if bit&(uint32(1)<<uint(item.ch)) == 0 { seen++; if seen == k { end = item.pos; break } }
                }
                prior := 0
                if i > base { prior = 1 }
                candidate := doneBefore+prior+1+parts[end]
                if candidate > answer { answer = candidate }
            }
        }
    }
    return answer
}