#include <stdlib.h>

int longestSubsequence(int* nums, int numsSize) {
    int* tails = malloc((size_t)numsSize * sizeof(*tails));
    int best = 0;

    // A nonzero AND means all chosen elements share at least one set bit.
    for (int bit = 0; bit < 30; ++bit) {
        const unsigned int flag = 1u << bit;
        int length = 0;
        for (int i = 0; i < numsSize; ++i) {
            const int value = nums[i];
            if (((unsigned int)value & flag) == 0) continue;

            // Replace the first tail >= value to keep the subsequence strictly increasing.
            int low = 0;
            int high = length;
            while (low < high) {
                int mid = low + (high - low) / 2;
                if (tails[mid] < value) low = mid + 1;
                else high = mid;
            }
            tails[low] = value;
            if (low == length) ++length;
        }
        if (length > best) best = length;
    }
    free(tails);
    return best;
}