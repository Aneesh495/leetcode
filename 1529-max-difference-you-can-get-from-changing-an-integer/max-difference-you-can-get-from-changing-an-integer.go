import "strconv"

func maxDiff(num int) int {
    digits := []byte(strconv.Itoa(num))
    maxDigits := append([]byte(nil), digits...)
    maxTarget := byte(0)
    for _, digit := range maxDigits {
        if digit != '9' { maxTarget = digit; break }
    }
    if maxTarget != 0 {
        for i := range maxDigits { if maxDigits[i] == maxTarget { maxDigits[i] = '9' } }
    }
    minDigits := append([]byte(nil), digits...)
    minTarget, minReplacement := byte(0), byte(0)
    if minDigits[0] != '1' {
        minTarget, minReplacement = minDigits[0], '1'
    } else {
        for i := 1; i < len(minDigits); i++ {
            if minDigits[i] != '0' && minDigits[i] != '1' {
                minTarget, minReplacement = minDigits[i], '0'
                break
            }
        }
    }
    if minTarget != 0 {
        for i := range minDigits { if minDigits[i] == minTarget { minDigits[i] = minReplacement } }
    }
    parse := func(value []byte) int {
        result := 0
        for _, digit := range value { result = result*10 + int(digit-'0') }
        return result
    }
    return parse(maxDigits) - parse(minDigits)
}