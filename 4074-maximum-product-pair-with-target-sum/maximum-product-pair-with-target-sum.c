#include <limits.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* maxProductPair(int* nums, int numsSize, int target, int* returnSize) {
    int* pair = malloc(2 * sizeof(*pair));
    pair[0] = pair[1] = -1;
    *returnSize = 2;
    int best = INT_MIN;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = 0; j < numsSize; ++j) {
            if (nums[i] <= nums[j] || nums[i] + nums[j] != target) continue;
            int product = nums[i] * nums[j];
            if (product > best) {
                best = product;
                pair[0] = i;
                pair[1] = j;
            }
        }
    }
    return pair;
}