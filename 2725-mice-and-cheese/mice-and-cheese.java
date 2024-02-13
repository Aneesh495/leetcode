class Solution {
    public int miceAndCheese(int[] reward1, int[] reward2, int k) {
        int n = reward1.length;
        int total = 0;
        int[] difference = new int[n];
        for (int i = 0; i < n; ++i) {
            total += reward2[i];
            difference[i] = reward1[i] - reward2[i];
        }
        Arrays.sort(difference);
        for (int i = n - k; i < n; ++i) total += difference[i];
        return total;
    }
}