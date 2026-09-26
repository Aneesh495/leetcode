class Solution {
    public long maxAlternatingSum(int[] nums, int k) {
        final int limit = 100_000;
        long[] up = new long[nums.length];
        long[] down = new long[nums.length];
        long[] downByValue = new long[limit + 1];
        long[] upByReverse = new long[limit + 1];
        long best = 0;
        for (int i = 0; i < nums.length; i++) {
            // A state joins the search trees once it is far enough from i.
            if (i >= k) {
                int eligible = i - k;
                update(downByValue, nums[eligible], down[eligible]);
                update(upByReverse, limit + 1 - nums[eligible], up[eligible]);
            }
            int value = nums[i];
            up[i] = value + maxPrefix(downByValue, value - 1);
            down[i] = value + maxPrefix(upByReverse, limit - value);
            best = Math.max(best, Math.max(up[i], down[i]));
        }
        return best;
    }

    private void update(long[] tree, int index, long value) {
        for (int i = index; i < tree.length; i += i & -i) {
            tree[i] = Math.max(tree[i], value);
        }
    }

    private long maxPrefix(long[] tree, int index) {
        long best = 0;
        for (int i = index; i > 0; i -= i & -i) {
            best = Math.max(best, tree[i]);
        }
        return best;
    }
}