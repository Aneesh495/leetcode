func countVowels(word string) int64 {
    var total int64
    for i := 0; i < len(word); i++ {
        switch word[i] {
        case 'a', 'e', 'i', 'o', 'u':
            // A substring containing i can start at any index through i
            // and end at any index from i onward.
            total += int64(i+1) * int64(len(word)-i)
        }
    }
    return total
}