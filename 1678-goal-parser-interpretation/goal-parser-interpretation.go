import "strings"

func interpret(command string) string {
    var result strings.Builder
    result.Grow(len(command))
    for i := 0; i < len(command); {
        // Inspect the first two characters to consume exactly one token.
        switch {
        case command[i] == 'G':
            result.WriteByte('G')
            i++
        case command[i+1] == ')':
            result.WriteByte('o')
            i += 2
        default:
            result.WriteString("al")
            i += 4
        }
    }
    return result.String()
}