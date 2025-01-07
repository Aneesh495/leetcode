int maxFrequencyElements(int* nums, int numsSize) {
    int freq[101] = {0};
    for (int i = 0; i < numsSize; ++i) freq[nums[i]]++;
    int maximum = 0, total = 0;
    for (int value = 1; value <= 100; ++value)
        if (freq[value] > maximum) maximum = freq[value];
    for (int value = 1; value <= 100; ++value)
        if (freq[value] == maximum) total += freq[value];
    return total;
}