class Solution {
    public long maxAlternatingSum(int[] nums) {
        long none = Long.MIN_VALUE / 4;
        long even = none, odd = none, usedEven = none, usedOdd = none;
        long best = none;
        for (int value : nums) {
            long nextOdd = Math.max(value, even + value);
            long nextEven = odd - value;
            // Either append with the current parity, or consume the one deletion here.
            long nextUsedOdd = Math.max(usedEven + value, odd);
            long nextUsedEven = Math.max(usedOdd - value, even);
            even = nextEven;
            odd = nextOdd;
            usedEven = nextUsedEven;
            usedOdd = nextUsedOdd;
            best = Math.max(best, Math.max(Math.max(even, odd), Math.max(usedEven, usedOdd)));
        }
        return best;
    }
}