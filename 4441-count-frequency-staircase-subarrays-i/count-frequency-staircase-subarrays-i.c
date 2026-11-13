#include <stdlib.h>

int countStaircase(int* nums, int numsSize) {
    const int values = 100001;
    int* memory = calloc(3 * values, sizeof(*memory));
    int* epoch = memory;
    int* expected = epoch + values;
    int* count = expected + values;
    int total = 0;
    for (int start = 0; start < numsSize; ++start) {
        int distinct = 0, mismatches = 0;
        for (int end = start; end < numsSize; ++end) {
            int value = nums[end];
            if (epoch[value] != start + 1) {
                epoch[value] = start + 1;
                expected[value] = ++distinct;
                count[value] = 0;
                ++mismatches;
            }
            // Only the new element's frequency can change the number of mismatches.
            mismatches -= count[value] != expected[value];
            ++count[value];
            mismatches += count[value] != expected[value];
            total += mismatches == 0;
        }
    }
    free(memory);
    return total;
}