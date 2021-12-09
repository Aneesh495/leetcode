func reformat(s string) string {
    letters, digits := make([]byte, 0), make([]byte, 0)
    for i := 0; i < len(s); i++ {
        if s[i] >= '0' && s[i] <= '9' {
            digits = append(digits, s[i])
        } else {
            letters = append(letters, s[i])
        }
    }
    first, second := letters, digits
    if len(second) > len(first) { first, second = digits, letters }
    if len(first)-len(second) > 1 { return "" }
    result := make([]byte, 0, len(s))
    for i := 0; i < len(first); i++ {
        result = append(result, first[i])
        if i < len(second) { result = append(result, second[i]) }
    }
    return string(result)
}