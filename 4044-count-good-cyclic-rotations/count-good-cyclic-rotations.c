int countGoodRotations(int* nums, int numsSize) {
    long long total = 0, halfSum = 0;
    int half = numsSize / 2;
    for (int i = 0; i < numsSize; ++i) {
        total += nums[i];
        if (i < half) halfSum += nums[i];
    }
    int answer = 0;
    for (int i = 0; i < numsSize; ++i) {
        answer += halfSum > total - halfSum;
        // Rotating one position slides the first half around the original array.
        halfSum += (long long)nums[(i + half) % numsSize] - nums[i];
    }
    return answer;
}