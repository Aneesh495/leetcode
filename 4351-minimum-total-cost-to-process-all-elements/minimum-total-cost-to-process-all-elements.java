class Solution {
    public int minimumCost(int[] nums, int k) {
        final long mod = 1_000_000_007;
        long resources = 0;
        for (int value : nums) resources += value;
        // Each refill gives the same number of resources, so the total demand fixes their count.
        long a = (resources - 1) / k;
        long b = a + 1;
        if (a % 2 == 0) a /= 2;
        else b /= 2;
        return (int)((a % mod) * (b % mod) % mod);
    }
}