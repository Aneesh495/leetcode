int chalkReplacer(int* chalk, int chalkSize, int k) {
    long long sum = 0;
    for (int i = 0; i < chalkSize; ++i) sum += chalk[i];
    long long remaining = (long long)k % sum;
    for (int i = 0; i < chalkSize; ++i) {
        if (remaining < chalk[i]) return i;
        remaining -= chalk[i];
    }
    return 0;
}