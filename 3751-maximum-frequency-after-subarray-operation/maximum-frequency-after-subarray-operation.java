class Solution {
    public int maxFrequency(int[] nums, int k) {
        int base = 0;
        for (int x : nums) if (x == k) base++;
        int answer = base;
        for (int target = 1; target <= 50; target++) {
            if (target == k) continue;
            int current = 0, best = 0;
            for (int x : nums) {
                current += (x == target ? 1 : (x == k ? -1 : 0));
                current = Math.max(current, 0);
                best = Math.max(best, current);
            }
            answer = Math.max(answer, base + best);
        }
        return answer;
    }
}