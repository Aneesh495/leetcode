import "strings"

func generateTag(caption string) string {
    words := strings.Fields(strings.ToLower(caption))
    tag := []byte{'#'}
    for index, word := range words {
        letters := []byte(word)
        if index > 0 && letters[0] >= 'a' && letters[0] <= 'z' {
            letters[0] -= 'a' - 'A'
        }
        remaining := 100 - len(tag)
        if len(letters) > remaining {
            tag = append(tag, letters[:remaining]...)
            break
        }
        tag = append(tag, letters...)
    }
    return string(tag)
}