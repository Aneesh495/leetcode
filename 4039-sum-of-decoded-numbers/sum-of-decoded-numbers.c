static long long powerMod(long long base, long long exponent, long long mod) {
    long long value = 1;
    while (exponent > 0) {
        if (exponent % 2 == 1) value = value * base % mod;
        base = base * base % mod;
        exponent /= 2;
    }
    return value;
}

int sumDecoded(long long* nums, int numsSize) {
    const long long mod = 1000000007;
    long long total = 0;
    for (int i = 0; i < numsSize; ++i) {
        int width = (int)(nums[i] % 10);
        long long data = nums[i] / 10;
        int digits = 0;
        for (long long copy = data; copy > 0; copy /= 10) ++digits;
        long long divider = 1;
        for (int remaining = digits - width; remaining > 0; --remaining) divider *= 10;
        // The divisor splits the leading width digits from the remaining digits.
        long long first = data / divider;
        long long second = data % divider;
        total = (total + powerMod(first, second, mod)) % mod;
    }
    return (int)total;
}