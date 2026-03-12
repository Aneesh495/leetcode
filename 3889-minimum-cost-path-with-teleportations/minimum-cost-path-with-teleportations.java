class Solution {
    public int minCost(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int total = m * n, maxValue = 0;
        for (int[] row : grid) for (int value : row) maxValue = Math.max(maxValue, value);
        final int INF = 1_000_000_000;
        int[] previous = new int[total];
        Arrays.fill(previous, INF);
        previous[0] = 0;
        for (int i = 0; i < total; i++) {
            int r = i / n, c = i % n;
            if (r + 1 < m) previous[i + n] = Math.min(previous[i + n], previous[i] + grid[r + 1][c]);
            if (c + 1 < n) previous[i + 1] = Math.min(previous[i + 1], previous[i] + grid[r][c + 1]);
        }
        for (int used = 1; used <= k; used++) {
            int[] best = new int[maxValue + 1];
            Arrays.fill(best, INF);
            for (int i = 0; i < total; i++) {
                int value = grid[i / n][i % n];
                best[value] = Math.min(best[value], previous[i]);
            }
            for (int value = maxValue - 1; value >= 0; value--) {
                best[value] = Math.min(best[value], best[value + 1]);
            }
            int[] current = previous.clone();
            for (int i = 0; i < total; i++) {
                int value = grid[i / n][i % n];
                current[i] = Math.min(current[i], best[value]);
            }
            for (int i = 0; i < total; i++) {
                int r = i / n, c = i % n;
                if (r + 1 < m) current[i + n] = Math.min(current[i + n], current[i] + grid[r + 1][c]);
                if (c + 1 < n) current[i + 1] = Math.min(current[i + 1], current[i] + grid[r][c + 1]);
            }
            previous = current;
        }
        return previous[total - 1];
    }
}