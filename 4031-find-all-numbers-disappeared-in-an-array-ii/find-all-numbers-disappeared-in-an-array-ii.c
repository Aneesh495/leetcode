#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** findDisappearedNumbers(int* nums, int numsSize, int lower, int upper, int* returnSize, int** returnColumnSizes) {
    unsigned char* present = calloc(upper + 1, sizeof(*present));
    for (int i = 0; i < numsSize; ++i) {
        if (nums[i] >= lower && nums[i] <= upper) present[nums[i]] = 1;
    }
    int capacity = upper - lower + 1;
    int** result = malloc(capacity * sizeof(*result));
    *returnColumnSizes = malloc(capacity * sizeof(**returnColumnSizes));
    *returnSize = 0;
    for (int i = lower; i <= upper;) {
        if (present[i]) {
            ++i;
            continue;
        }
        int start = i;
        while (i <= upper && !present[i]) ++i;
        int at = (*returnSize)++;
        result[at] = malloc(2 * sizeof(*result[at]));
        result[at][0] = start;
        result[at][1] = i - 1;
        (*returnColumnSizes)[at] = 2;
    }
    free(present);
    return result;
}