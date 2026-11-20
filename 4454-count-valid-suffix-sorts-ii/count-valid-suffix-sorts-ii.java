class Solution {
    public int[] countSuffix(int[] nums, int[] target) {
        int n = nums.length, m = target.length;
        int[] joined = new int[n + 1 + m];
        System.arraycopy(nums, 0, joined, 0, n);
        System.arraycopy(target, 0, joined, n + 1, m);
        int[] z = new int[joined.length];
        for (int i = 1, left = 0, right = 0; i < z.length; i++) {
            if (i < right) z[i] = Math.min(right - i, z[i - left]);
            while (i + z[i] < z.length && joined[z[i]] == joined[i + z[i]]) z[i]++;
            if (i + z[i] > right) {
                left = i;
                right = i + z[i];
            }
        }
        int[] suffixStart = new int[m];
        for (int i = 1; i < m; i++) suffixStart[i] = target[i - 1] < target[i] ? i : suffixStart[i - 1];
        int[] balance = new int[100001];
        int differs = 0;
        for (int i = 0; i < n; i++) {
            differs += apply(balance, nums[i], 1);
            differs += apply(balance, target[i], -1);
        }
        int[] answer = new int[m - n + 1];
        for (int i = 0; i < answer.length; i++) {
            if (differs == 0) {
                // With equal window multisets, matching prefixes also leave equal suffix multisets.
                int firstCut = Math.max(0, suffixStart[i + n - 1] - i);
                int lastCut = Math.min(n - 1, z[n + 1 + i]);
                answer[i] = Math.max(0, lastCut - firstCut + 1);
            }
            if (i + n < m) {
                differs += apply(balance, target[i], 1);
                differs += apply(balance, target[i + n], -1);
            }
        }
        return answer;
    }

    private int apply(int[] balance, int value, int delta) {
        int before = balance[value] == 0 ? 0 : 1;
        balance[value] += delta;
        return (balance[value] == 0 ? 0 : 1) - before;
    }
}