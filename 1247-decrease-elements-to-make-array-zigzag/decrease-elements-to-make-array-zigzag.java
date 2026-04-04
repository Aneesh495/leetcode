
class Solution {
    public int movesToMakeZigzag(int[] nums) {
        return Math.min(helper(nums, 0), helper(nums, 1));
    }

    private int helper(int[] nums, int start) {
        int n = nums.length, moves = 0;
        for (int i = start; i < n; i += 2) {
            int left = i > 0 ? nums[i - 1] : Integer.MAX_VALUE;
            int right = i + 1 < n ? nums[i + 1] : Integer.MAX_VALUE;
            int minNeighbor = Math.min(left, right);
            if (nums[i] >= minNeighbor)
                moves += nums[i] - minNeighbor + 1;
        }
        return moves;
    }
}
