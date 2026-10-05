import java.util.Arrays;

class Solution {
    public long maximizeSum(int[] nums, int k) {
        long total = 0;
        int[] gain = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            int number = nums[i];
            total += number;
            char[] digits = Integer.toString(number).toCharArray();
            Arrays.sort(digits);
            int best = 0;
            for (int p = digits.length - 1; p >= 0; p--) best = best * 10 + digits[p] - '0';
            gain[i] = best - number;
        }
        // Each operation improves a separate element, so take the largest gains.
        Arrays.sort(gain);
        for (int i = gain.length - 1; i >= gain.length - k; i--) total += gain[i];
        return total;
    }
}