#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* transformStr(char* s, char** strs, int strsSize, int* returnSize) {
    int n = (int)strlen(s);
    int* prefix = malloc((n + 1) * sizeof(*prefix));
    prefix[0] = 0;
    for (int i = 0; i < n; ++i) prefix[i + 1] = prefix[i] + (s[i] == '0');
    bool* result = malloc(strsSize * sizeof(*result));
    *returnSize = strsSize;
    for (int row = 0; row < strsSize; ++row) {
        const char* pattern = strs[row];
        int fixed = 0, unknown = 0;
        for (int i = 0; i < n; ++i) {
            fixed += pattern[i] == '0';
            unknown += pattern[i] == '?';
        }
        int extra = prefix[n] - fixed;
        result[row] = extra >= 0 && extra <= unknown;
        if (!result[row]) continue;
        int zeros = 0;
        for (int i = 0; i < n; ++i) {
            if (pattern[i] == '0') ++zeros;
            else if (pattern[i] == '?' && extra > 0) { ++zeros; --extra; }
            // Sorting a binary subsequence can move zeros earlier, never later.
            if (zeros < prefix[i + 1]) { result[row] = false; break; }
        }
    }
    free(prefix);
    return result;
}