public class Solution {
    public long MaximumSumOfHeights(IList<int> maxHeights) {
        int n = maxHeights.Count;
        long best = 0;
        for (int peak = 0; peak < n; peak++) {
            long sum = maxHeights[peak];
            int height = maxHeights[peak];
            for (int i = peak - 1; i >= 0; i--) {
                height = Math.Min(height, maxHeights[i]);
                sum += height;
            }
            height = maxHeights[peak];
            for (int i = peak + 1; i < n; i++) {
                height = Math.Min(height, maxHeights[i]);
                sum += height;
            }
            best = Math.Max(best, sum);
        }
        return best;
    }
}