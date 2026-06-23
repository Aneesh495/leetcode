#include <stdlib.h>
#include <string.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** largestString(int* nums, int numsSize, int* returnSize) {
    char** result = malloc(numsSize * sizeof(*result));
    *returnSize = numsSize;
    for (int i = 0; i < numsSize; ++i) {
        int remaining = nums[i];
        char buffer[32];
        int length = 0;
        // A letter at offset b consumes exactly 2^b original a's.
        for (int b = 25; b >= 0; --b) {
            int weight = 1 << b;
            while (remaining >= weight) {
                buffer[length++] = (char)('a' + b);
                remaining -= weight;
            }
        }
        buffer[length] = '\0';
        result[i] = malloc(length + 1);
        memcpy(result[i], buffer, length + 1);
    }
    return result;
}