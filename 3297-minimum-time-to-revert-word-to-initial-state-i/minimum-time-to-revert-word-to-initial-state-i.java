class Solution {
    public int minimumTimeToInitialState(String word, int k) {
        int n = word.length();
        // After t operations, the surviving suffix must match the original prefix.
        for (int removed = k; removed < n; removed += k) {
            if (word.regionMatches(removed, word, 0, n - removed)) return removed / k;
        }
        return (n + k - 1) / k;
    }
}