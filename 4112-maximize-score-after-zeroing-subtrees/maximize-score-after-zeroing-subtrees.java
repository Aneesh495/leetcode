import java.util.Arrays;

class Solution {
    public int maxScore(int[] parent, int[] op, int[] score) {
        int n = parent.length;
        int[] children = new int[n];
        for (int i = 1; i < n; i++) children[parent[i]]++;
        int[] queue = new int[n];
        int end = 0;
        for (int i = 0; i < n; i++) if (children[i] == 0) queue[end++] = i;
        long[] sum = new long[n];
        long[] minimum = new long[n];
        Arrays.fill(minimum, Long.MAX_VALUE);
        for (int head = 0; head < end; head++) {
            int node = queue[head];
            long best = score[node] + sum[node];
            // Zeroing a child removes its optimized subtree contribution.
            if (minimum[node] != Long.MAX_VALUE) {
                best -= op[node] == 1 ? minimum[node] : Math.min(0L, minimum[node]);
            }
            int p = parent[node];
            if (p == -1) return (int) best;
            sum[p] += best;
            minimum[p] = Math.min(minimum[p], best);
            if (--children[p] == 0) queue[end++] = p;
        }
        return 0;
    }
}