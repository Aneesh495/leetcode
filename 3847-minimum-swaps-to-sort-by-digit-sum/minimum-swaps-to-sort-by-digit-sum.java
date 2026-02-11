class Solution {
    private int digitSum(int x) {
        int sum = 0;
        while (x > 0) { sum += x % 10; x /= 10; }
        return sum;
    }

    public int minSwaps(int[] nums) {
        Integer[] sorted = Arrays.stream(nums).boxed().toArray(Integer[]::new);
        Arrays.sort(sorted, (a, b) -> {
            int sa = digitSum(a), sb = digitSum(b);
            return sa != sb ? Integer.compare(sa, sb) : Integer.compare(a, b);
        });
        Map<Integer, Integer> target = new HashMap<>();
        for (int i = 0; i < sorted.length; ++i) target.put(sorted[i], i);
        int[] next = new int[nums.length];
        for (int i = 0; i < nums.length; ++i) next[i] = target.get(nums[i]);
        boolean[] seen = new boolean[nums.length];
        int swaps = 0;
        for (int i = 0; i < nums.length; ++i) {
            if (seen[i]) continue;
            int length = 0, j = i;
            while (!seen[j]) { seen[j] = true; ++length; j = next[j]; }
            swaps += length - 1;
        }
        return swaps;
    }
}