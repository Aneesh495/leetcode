static int divisor(int a, int b) {
    while (b != 0) {
        int remainder = a % b;
        a = b;
        b = remainder;
    }
    return a;
}

long long maxPairStrength(int* nums, int numsSize) {
    long long best = 0;
    for (int i = 0; i < numsSize; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            int common = divisor(nums[i], nums[j]);
            long long strength = (long long)(nums[i] / common) * (nums[j] / common);
            if (strength > best) best = strength;
        }
    }
    return best;
}