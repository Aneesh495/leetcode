class Solution {
    public int countPermutations(int[] complexity) {
        final int mod = 1_000_000_007;
        long ways = 1;
        for (int i = 1; i < complexity.length; i++) {
            // Every unlocking chain starts at 0 and strictly increases in complexity.
            if (complexity[i] <= complexity[0]) {
                return 0;
            }
            // Otherwise 0 can unlock every computer directly, in any order.
            ways = ways * i % mod;
        }
        return (int) ways;
    }
}