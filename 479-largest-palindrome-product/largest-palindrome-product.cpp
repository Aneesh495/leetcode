class Solution {
public:
    int largestPalindrome(int n) {
        if (n == 1) return 9;

        long long bound = 1;
        for (int i = 0; i < n; ++i) bound *= 10;
        const long long high = bound - 1;
        const long long low = bound / 10;

        // Within each digit length, larger left halves give larger palindromes.
        for (int digits : {2 * n, 2 * n - 1}) {
            const long long step = digits % 2 == 0 ? 11 : 1;
            for (long long half = high; half >= low; --half) {
                long long palindrome = half;
                for (long long rest = digits % 2 == 0 ? half : half / 10;
                     rest > 0; rest /= 10) {
                    palindrome = palindrome * 10 + rest % 10;
                }
                if (palindrome > high * high) continue;
                const long long minFactor = max(low, (palindrome + high - 1) / high);
                const long long maxFactor = min(high, palindrome / low);
                // Every even-digit palindrome is divisible by 11, so one factor is too.
                for (long long factor = maxFactor / step * step; factor >= minFactor; factor -= step) {
                    if (palindrome % factor == 0) return palindrome % 1337;
                }
            }
        }
        return 0;
    }
};