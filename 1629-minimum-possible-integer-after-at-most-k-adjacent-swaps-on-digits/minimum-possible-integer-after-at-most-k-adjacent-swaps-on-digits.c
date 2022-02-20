#include <stdlib.h>
#include <string.h>

static int removedBefore(const int* tree, int index) {
    int count = 0;
    for (int i = index; i > 0; i -= i & -i) count += tree[i];
    return count;
}

static void removeAt(int* tree, int n, int index) {
    for (int i = index + 1; i <= n; i += i & -i) ++tree[i];
}

char* minInteger(char* num, int k) {
    const int n = (int)strlen(num);
    int* positions = malloc(10 * n * sizeof(*positions));
    int* removed = calloc(n + 1, sizeof(*removed));
    char* result = malloc(n + 1);
    int size[10] = {0}, next[10] = {0};
    for (int i = 0; i < n; ++i) {
        int digit = num[i] - '0';
        positions[digit * n + size[digit]++] = i;
    }
    for (int out = 0; out < n; ++out) {
        for (int digit = 0; digit < 10; ++digit) {
            if (next[digit] == size[digit]) continue;
            int position = positions[digit * n + next[digit]];
            // Previously placed digits to the left no longer need to be crossed.
            int cost = position - removedBefore(removed, position);
            if (cost > k) continue;
            k -= cost;
            result[out] = (char)('0' + digit);
            ++next[digit];
            removeAt(removed, n, position);
            break;
        }
    }
    result[n] = '\0';
    free(positions);
    free(removed);
    return result;
}