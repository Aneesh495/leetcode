import java.util.Arrays;

class Solution {
    public long[] minTimeMaxPower(int n, int[][] edges, int power, int[] cost, int source, int target) {
        int size = cost.length;
        int[] head = new int[size], next = new int[edges.length];
        Arrays.fill(head, -1);
        for (int i = 0; i < edges.length; i++) {
            int node = edges[i][0];
            next[i] = head[node];
            head[node] = i;
        }
        long infinity = Long.MAX_VALUE / 4;
        long[][] time = new long[size][power + 1];
        for (long[] row : time) Arrays.fill(row, infinity);
        time[source][power] = 0;
        // Every traversal strictly reduces power, so descending power is a topological order.
        for (int left = power; left >= 0; left--) {
            for (int node = 0; node < size; node++) {
                int after = left - cost[node];
                if (after < 0 || time[node][left] == infinity) continue;
                for (int i = head[node]; i != -1; i = next[i]) {
                    int to = edges[i][1];
                    time[to][after] = Math.min(time[to][after], time[node][left] + edges[i][2]);
                }
            }
        }
        long best = infinity;
        int left = -1;
        for (int p = power; p >= 0; p--) {
            if (time[target][p] < best) {
                best = time[target][p];
                left = p;
            }
        }
        return new long[]{left == -1 ? -1 : best, left};
    }
}