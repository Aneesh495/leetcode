class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] count = new int[101];
        for (int value : nums) count[value]++;
        int[] result = new int[nums.length];
        int size = 0;
        // Each pass emits one remaining copy of every value in sorted order.
        while (size < result.length) {
            for (int value = 1; value <= 100; value++) {
                if (count[value] > 0) {
                    count[value]--;
                    result[size++] = value;
                }
            }
        }
        return result;
    }
}