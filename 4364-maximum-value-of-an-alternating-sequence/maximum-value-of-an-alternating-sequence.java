class Solution {
    public long maximumValue(int n, int s, int m) {
        if (n == 1) return s;
        // Start with the largest upward step, then alternate a one-unit drop and an m-unit rise.
        return (long) s + m + (long) ((n - 2) / 2) * (m - 1);
    }
}