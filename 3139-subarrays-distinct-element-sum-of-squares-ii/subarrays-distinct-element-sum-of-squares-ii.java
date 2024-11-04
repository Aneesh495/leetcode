import java.util.Arrays;

class Solution {
    public int sumCounts(int[] nums) {
        final long mod = 1_000_000_007;
        int[] last = new int[100_001];
        Arrays.fill(last, -1);
        long[] firstTree = new long[nums.length + 2];
        long[] secondTree = new long[nums.length + 2];
        long answer = 0;
        long squares = 0;

        for (int i = 0; i < nums.length; i++) {
            // A new value increments the distinct counts for starts after its last occurrence.
            int left = last[nums[i]] + 2;
            int right = i + 1;
            long prior = total(firstTree, secondTree, right) - total(firstTree, secondTree, left - 1);
            squares = (squares + 2 * prior + right - left + 1) % mod;
            answer = (answer + squares) % mod;

            add(firstTree, left, 1);
            add(firstTree, right + 1, -1);
            add(secondTree, left, left - 1);
            add(secondTree, right + 1, -right);
            last[nums[i]] = i;
        }
        return (int) answer;
    }

    private void add(long[] tree, int index, long value) {
        for (int i = index; i < tree.length; i += i & -i) tree[i] += value;
    }

    private long prefix(long[] tree, int index) {
        long sum = 0;
        for (int i = index; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }

    private long total(long[] first, long[] second, int index) {
        return index * prefix(first, index) - prefix(second, index);
    }
}