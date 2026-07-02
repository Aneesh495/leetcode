class Solution {
    public long countNoZeroPairs(long n) {
        // Each mask states which addends still have a digit at this decimal position.
        long[][] dp = new long[4][2];
        dp[3][0] = 1;
        for (long remaining = n; remaining > 0; remaining /= 10) {
            int target = (int)(remaining % 10);
            long[][] next = new long[4][2];
            for (int active = 0; active < 4; active++) {
                boolean leftActive = (active & 1) != 0;
                boolean rightActive = (active & 2) != 0;
                for (int carry = 0; carry <= 1; carry++) {
                    long ways = dp[active][carry];
                    if (ways == 0) continue;
                    for (int a = leftActive ? 1 : 0; a <= (leftActive ? 9 : 0); a++) {
                        for (int b = rightActive ? 1 : 0; b <= (rightActive ? 9 : 0); b++) {
                            int sum = a + b + carry;
                            if (sum % 10 != target) continue;
                            // Any still-active addend may end immediately after this digit.
                            for (int continuing = active; ; continuing = (continuing - 1) & active) {
                                next[continuing][sum / 10] += ways;
                                if (continuing == 0) break;
                            }
                        }
                    }
                }
            }
            dp = next;
        }
        return dp[0][0];
    }
}