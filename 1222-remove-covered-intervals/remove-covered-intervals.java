import java.util.Arrays;

class Solution {
    public int removeCoveredIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(b[1], a[1]);
        });
        int remaining = 0;
        int farthestEnd = -1;
        for (int[] interval : intervals) {
            if (interval[1] > farthestEnd) {
                remaining++;
                farthestEnd = interval[1];
            }
        }
        return remaining;
    }
}