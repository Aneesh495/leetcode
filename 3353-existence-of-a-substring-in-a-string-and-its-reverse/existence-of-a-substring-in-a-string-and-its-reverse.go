func isSubstringPresent(s string) bool {
    var present [26][26]bool
    for i := 0; i+1 < len(s); i++ {
        a, b := s[i]-'a', s[i+1]-'a'
        present[a][b] = true
    }
    for a := 0; a < 26; a++ {
        for b := 0; b < 26; b++ {
            if present[a][b] && present[b][a] {
                return true
            }
        }
    }
    return false
}