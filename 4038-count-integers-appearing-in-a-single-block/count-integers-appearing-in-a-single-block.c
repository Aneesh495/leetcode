int countSpecialIntegers(int* nums, int numsSize) {
    int blocks[101] = {0};
    for (int i = 0; i < numsSize; ++i) {
        // A value starts a new block only when it differs from its predecessor.
        if (i == 0 || nums[i] != nums[i - 1]) ++blocks[nums[i]];
    }
    int total = 0;
    for (int value = 1; value <= 100; ++value) total += blocks[value] == 1;
    return total;
}