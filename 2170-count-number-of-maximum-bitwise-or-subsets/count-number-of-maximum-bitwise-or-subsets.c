static int countChoices(const int* nums, int size, int index, int bits, int target) {
    // Once the target is reached, every selection from the suffix works.
    if (bits == target) return 1 << (size - index);
    if (index == size) return 0;
    return countChoices(nums, size, index + 1, bits, target)
         + countChoices(nums, size, index + 1, bits | nums[index], target);
}

int countMaxOrSubsets(int* nums, int numsSize) {
    int target = 0;
    for (int i = 0; i < numsSize; ++i) target |= nums[i];
    return countChoices(nums, numsSize, 0, 0, target);
}