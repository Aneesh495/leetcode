public class Solution {
    private const long Mod = 1_000_000_007;
    private long Pow(long value, long exponent) {
        long result = 1;
        while (exponent > 0) {
            if ((exponent & 1) == 1) result = result * value % Mod;
            value = value * value % Mod;
            exponent >>= 1;
        }
        return result;
    }
    public int MaxNiceDivisors(int primeFactors) {
        if (primeFactors == 1) return 1;
        if (primeFactors % 3 == 0) return (int)Pow(3, primeFactors / 3);
        if (primeFactors % 3 == 1)
            return (int)(4 * Pow(3, (primeFactors - 4) / 3) % Mod);
        return (int)(2 * Pow(3, primeFactors / 3) % Mod);
    }
}