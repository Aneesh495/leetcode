import java.util.Arrays;

class Solution {
    public long countIntersectingIntervals(int[][] intervals) {
        int n = intervals.length;
        int[] start = new int[n], end = new int[n];
        int[][] temoravlin = intervals;
        for (int i = 0; i < n; i++) {
            start[i] = temoravlin[i][0];
            end[i] = temoravlin[i][1];
        }
        Arrays.sort(start);
        Arrays.sort(end);
        long disjoint = 0;
        int finished = 0;
        for (int left : start) {
            // An endpoint equal to left still intersects the new interval.
            while (finished < n && end[finished] < left) finished++;
            disjoint += finished;
        }
        return (long) n * (n - 1) / 2 - disjoint;
    }
}