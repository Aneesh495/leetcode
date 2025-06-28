#include <stdlib.h>
#include <string.h>

static int chooseCapped(int n, int r, int cap) {
    if (r > n - r) r = n - r;
    long long count = 1;
    for (int i = 1; i <= r; ++i) {
        count = count * (n - r + i) / i;
        if (count >= cap) return cap;
    }
    return (int)count;
}

static int permutationsCapped(const int* frequency, int cap) {
    int used = 0, count = 1;
    for (int letter = 0; letter < 26; ++letter) {
        int copies = frequency[letter];
        if (copies == 0) continue;
        int need = (cap + count - 1) / count;
        count *= chooseCapped(used + copies, copies, need);
        if (count >= cap) return cap;
        used += copies;
    }
    return count;
}

char* smallestPalindrome(char* s, int k) {
    int n = (int)strlen(s);
    char* result = malloc(n + 1);
    int frequency[26] = {0};
    for (int i = 0; i < n; ++i) ++frequency[s[i] - 'a'];
    for (int i = 0; i < 26; ++i) {
        if (frequency[i] & 1) result[n / 2] = (char)('a' + i);
        frequency[i] /= 2;
    }
    if (permutationsCapped(frequency, k) < k) {
        result[0] = '\0';
        return result;
    }
    // Rank the first half. Its mirror determines the other half uniquely.
    for (int i = 0; i < n / 2; ++i) {
        for (int letter = 0; letter < 26; ++letter) {
            if (frequency[letter] == 0) continue;
            --frequency[letter];
            int block = permutationsCapped(frequency, k);
            if (block >= k) {
                result[i] = result[n - 1 - i] = (char)('a' + letter);
                break;
            }
            k -= block;
            ++frequency[letter];
        }
    }
    result[n] = '\0';
    return result;
}