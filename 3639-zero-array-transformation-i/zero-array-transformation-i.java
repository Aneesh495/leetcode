class Solution {
    public boolean isZeroArray(int[] nums, int[][] queries) {
        int[] difference = new int[nums.length + 1];
        for (int[] query : queries) {
            ++difference[query[0]];
            --difference[query[1] + 1];
        }
        int available = 0;
        for (int i = 0; i < nums.length; ++i) {
            available += difference[i];
            if (nums[i] > available) return false;
        }
        return true;
    }
}