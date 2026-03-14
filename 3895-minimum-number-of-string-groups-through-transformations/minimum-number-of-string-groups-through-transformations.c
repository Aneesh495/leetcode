#include <stdlib.h>
#include <string.h>

static int leastRotation(const char* word, int parity, int length) {
    if (length <= 1) return 0;
    int left = 0, right = 1, matched = 0;
    while (left < length && right < length && matched < length) {
        char a = word[parity + 2 * ((left + matched) % length)];
        char b = word[parity + 2 * ((right + matched) % length)];
        if (a == b) {
            ++matched;
            continue;
        }
        if (a > b) {
            left += matched + 1;
            if (left <= right) left = right + 1;
        } else {
            right += matched + 1;
            if (right <= left) right = left + 1;
        }
        matched = 0;
    }
    return left < right ? left : right;
}

static int compareKeys(const void* a, const void* b) {
    return strcmp(*(const char* const*)a, *(const char* const*)b);
}

int minimumGroups(char** words, int wordsSize) {
    char** keys = malloc(wordsSize * sizeof(*keys));
    for (int i = 0; i < wordsSize; ++i) {
        const char* word = words[i];
        int length = (int)strlen(word);
        keys[i] = malloc(length + 2);
        int at = 0;
        // Each parity subsequence has its own canonical cyclic rotation.
        for (int parity = 0; parity < 2; ++parity) {
            int count = (length + 1 - parity) / 2;
            int first = leastRotation(word, parity, count);
            for (int p = 0; p < count; ++p) {
                keys[i][at++] = word[parity + 2 * ((first + p) % count)];
            }
            keys[i][at++] = parity == 0 ? '#' : '\0';
        }
    }
    qsort(keys, wordsSize, sizeof(*keys), compareKeys);
    int groups = 1;
    for (int i = 1; i < wordsSize; ++i) groups += strcmp(keys[i - 1], keys[i]) != 0;
    for (int i = 0; i < wordsSize; ++i) free(keys[i]);
    free(keys);
    return groups;
}