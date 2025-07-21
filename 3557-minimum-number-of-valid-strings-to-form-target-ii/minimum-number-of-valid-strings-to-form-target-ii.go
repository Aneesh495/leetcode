func minValidStrings(words []string, target string) int {
    const mod1 int64 = 1000000007
    const mod2 int64 = 1000000009
    const base int64 = 911382323
    type pair struct { a, b int64 }
    prefixes := make(map[pair]struct{})
    for _, word := range words {
        var h1, h2 int64
        for i := 0; i < len(word); i++ {
            value := int64(word[i]-'a'+1)
            h1 = (h1*base + value) % mod1
            h2 = (h2*base + value) % mod2
            prefixes[pair{h1, h2}] = struct{}{}
        }
    }
    n := len(target)
    pow1, pow2 := make([]int64, n+1), make([]int64, n+1)
    pref1, pref2 := make([]int64, n+1), make([]int64, n+1)
    pow1[0], pow2[0] = 1, 1
    for i := 0; i < n; i++ {
        pow1[i+1] = pow1[i] * base % mod1
        pow2[i+1] = pow2[i] * base % mod2
        value := int64(target[i]-'a'+1)
        pref1[i+1] = (pref1[i]*base + value) % mod1
        pref2[i+1] = (pref2[i]*base + value) % mod2
    }
    maxLen := make([]int, n)
    for i := 0; i < n; i++ {
        low, high := 0, n-i
        for low < high {
            mid := (low + high + 1) / 2
            h1 := (pref1[i+mid] - pref1[i]*pow1[mid]%mod1 + mod1) % mod1
            h2 := (pref2[i+mid] - pref2[i]*pow2[mid]%mod2 + mod2) % mod2
            if _, ok := prefixes[pair{h1, h2}]; ok { low = mid } else { high = mid - 1 }
        }
        maxLen[i] = low
    }
    jumps, currentEnd, farthest := 0, 0, 0
    for i := 0; i < n; i++ {
        if i > farthest { return -1 }
        if i+maxLen[i] > farthest { farthest = i + maxLen[i] }
        if i == currentEnd {
            jumps++
            currentEnd = farthest
            if currentEnd >= n { return jumps }
        }
    }
    return -1
}