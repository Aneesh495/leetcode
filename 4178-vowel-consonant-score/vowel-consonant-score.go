func vowelConsonantScore(s string) int {
    vowels, consonants := 0, 0
    for i := 0; i < len(s); i++ {
        ch := s[i]
        switch ch {
        case 'a', 'e', 'i', 'o', 'u':
            vowels++
        default:
            if ch >= 'a' && ch <= 'z' {
                consonants++
            }
        }
    }
    if consonants == 0 {
        return 0
    }
    return vowels / consonants
}