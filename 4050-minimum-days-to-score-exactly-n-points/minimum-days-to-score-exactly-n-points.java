import java.util.Arrays;

class Solution {
    public int minDays(int n) {
        int[] days = new int[n + 1];
        Arrays.fill(days, 2 * n + 1);
        days[0] = 0;
        for (int length = 1; length * (length + 1) / 2 <= n; length++) {
            int gained = length * (length + 1) / 2;
            // Charge every streak for a reset, then remove the final reset below.
            for (int score = gained; score <= n; score++) {
                days[score] = Math.min(days[score], days[score - gained] + length + 1);
            }
        }
        return days[n] - 1;
    }
}