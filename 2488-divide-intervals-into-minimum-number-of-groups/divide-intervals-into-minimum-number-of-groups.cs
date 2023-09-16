public class Solution {
    public int MinGroups(int[][] intervals) {
        int[] delta = new int[1_000_002];
        foreach (int[] interval in intervals) {
            delta[interval[0]]++;
            delta[interval[1] + 1]--;
        }
        int active = 0, answer = 0;
        for (int x = 1; x <= 1_000_000; x++) {
            active += delta[x];
            if (active > answer) answer = active;
        }
        return answer;
    }
}