static const long long MOD = 1000000007;

typedef struct { long long value, successor; } FibonacciPair;

static FibonacciPair fibonacci(long long n) {
    if (n == 0) return (FibonacciPair){0, 1};
    FibonacciPair half = fibonacci(n / 2);
    long long a = half.value;
    long long b = half.successor;
    long long even = a * ((2 * b - a + MOD) % MOD) % MOD;
    long long odd = (a * a + b * b) % MOD;
    if (n % 2 == 0) return (FibonacciPair){even, odd};
    return (FibonacciPair){odd, (even + odd) % MOD};
}

int countGoodStrings(long long n) {
    // Every maximal run is odd. Compositions into odd parts count as Fibonacci(n).
    return (int)(2 * fibonacci(n).value % MOD);
}