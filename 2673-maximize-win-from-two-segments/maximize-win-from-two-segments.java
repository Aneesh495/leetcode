class Solution {
    public int maximizeWin(int[] prizePositions, int k) {
        int n = prizePositions.length;
        int[] bestPrefix = new int[n + 1];
        int left = 0;
        int answer = 0;
        for (int right = 0; right < n; right++) {
            while (prizePositions[right] - prizePositions[left] > k) left++;
            int covered = right - left + 1;
            answer = Math.max(answer, covered + bestPrefix[left]);
            bestPrefix[right + 1] = Math.max(bestPrefix[right], covered);
        }
        return answer;
    }
}