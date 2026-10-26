class Solution {
    public int maxDigitRange(int[] nums) {
        int best = -1, sum = 0;
        for (int number : nums) {
            int low = 9, high = 0;
            for (int rest = number; rest > 0; rest /= 10) {
                int digit = rest % 10;
                low = Math.min(low, digit);
                high = Math.max(high, digit);
            }
            int range = high - low;
            if (range > best) {
                best = range;
                sum = number;
            } else if (range == best) {
                sum += number;
            }
        }
        return sum;
    }
}