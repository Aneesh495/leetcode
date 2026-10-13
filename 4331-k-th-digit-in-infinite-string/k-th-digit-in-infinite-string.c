int kthDigit(long long k) {
    long long first = 1;
    int digits = 1;
    while (k > 9 * first * digits) {
        k -= 9 * first * digits;
        first *= 10;
        ++digits;
    }
    long long number = first + (k - 1) / digits;
    long long block = number / 10;
    // Digit widths are constant in a block. Reverse only the position within odd blocks.
    if (block % 2 == 1) number = 10 * block + 9 - number % 10;
    int offset = (int)((k - 1) % digits);
    for (int j = digits - 1; j > offset; --j) number /= 10;
    return (int)(number % 10);
}