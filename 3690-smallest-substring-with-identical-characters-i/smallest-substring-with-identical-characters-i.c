#include <string.h>

static int feasible(char* s, int n, int limit, int numOps) {
    if (limit == 1) {
        int mismatch0 = 0, mismatch1 = 0;
        for (int i = 0; i < n; i++) {
            char expected0 = (i % 2 == 0) ? '0' : '1';
            char expected1 = (i % 2 == 0) ? '1' : '0';
            if (s[i] != expected0) mismatch0++;
            if (s[i] != expected1) mismatch1++;
        }
        return (mismatch0 < mismatch1 ? mismatch0 : mismatch1) <= numOps;
    }
    int operations = 0, run = 0;
    for (int i = 0; i < n; i++) {
        run++;
        if (i == n - 1 || s[i] != s[i + 1]) {
            operations += run / (limit + 1);
            run = 0;
            if (operations > numOps) return 0;
        }
    }
    return operations <= numOps;
}

int minLength(char* s, int numOps) {
    int n = (int)strlen(s);
    int low = 1, high = n;
    while (low < high) {
        int mid = low + (high - low) / 2;
        if (feasible(s, n, mid, numOps)) high = mid;
        else low = mid + 1;
    }
    return low;
}