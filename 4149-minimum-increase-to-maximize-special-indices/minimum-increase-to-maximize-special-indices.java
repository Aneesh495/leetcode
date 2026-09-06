class Solution {
    public long minIncrease(int[] nums) {
        int olderCount = 0, previousCount = 0;
        long olderCost = 0, previousCost = 0;
        for (int i = 1; i + 1 < nums.length; i++) {
            int pickCount = olderCount + 1;
            long increase = Math.max(0L, 1L + Math.max(nums[i-1], nums[i+1]) - nums[i]);
            long pickCost = olderCost + increase;
            // Two peaks cannot be adjacent. First maximize count, then minimize total increase.
            int count = previousCount;
            long cost = previousCost;
            if (pickCount > count || (pickCount == count && pickCost < cost)) {
                count = pickCount;
                cost = pickCost;
            }
            olderCount = previousCount;
            olderCost = previousCost;
            previousCount = count;
            previousCost = cost;
        }
        return previousCost;
    }
}