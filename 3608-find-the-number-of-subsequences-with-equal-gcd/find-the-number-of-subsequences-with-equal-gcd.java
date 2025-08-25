class Solution {
    private static final int MOD = 1_000_000_007;

    public int subsequencePairCount(int[] nums) {
        int largest = 0;
        for (int number : nums) largest = Math.max(largest, number);
        int size = largest + 1;
        int[][] gcd = new int[size][size];
        for (int a = 0; a < size; a++) {
            for (int b = 0; b < size; b++) {
                int x = a, y = b;
                while (y != 0) {
                    int r = x % y;
                    x = y;
                    y = r;
                }
                gcd[a][b] = x;
            }
        }

        int[][] dp = new int[size][size];
        dp[0][0] = 1;
        for (int value : nums) {
            int[][] next = new int[size][size];
            for (int a = 0; a < size; a++) {
                for (int b = 0; b < size; b++) {
                    int count = dp[a][b];
                    if (count == 0) continue;
                    // Assign each index to neither subsequence, the first, or the second.
                    add(next, a, b, count);
                    add(next, gcd[a][value], b, count);
                    add(next, a, gcd[b][value], count);
                }
            }
            dp = next;
        }
        int answer = 0;
        for (int g = 1; g < size; g++) answer = (answer + dp[g][g]) % MOD;
        return answer;
    }

    private void add(int[][] dp, int a, int b, int count) {
        int total = dp[a][b] + count;
        dp[a][b] = total >= MOD ? total - MOD : total;
    }
}