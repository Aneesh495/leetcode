#include <stdbool.h>
#include <string.h>

bool canConvertString(char* s, char* t, int k) {
    if (strlen(s) != strlen(t)) return false;
    int used[26] = {0};
    for (int i = 0; s[i] != '\0'; ++i) {
        int shift = (t[i] - s[i] + 26) % 26;
        if (shift == 0) continue;
        // A shift of d can use move numbers d, d+26, d+52, and so on.
        int move = shift + 26 * used[shift]++;
        if (move > k) return false;
    }
    return true;
}