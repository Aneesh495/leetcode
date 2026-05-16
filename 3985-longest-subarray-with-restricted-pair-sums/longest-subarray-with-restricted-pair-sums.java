class Solution {
    public int maxSubarray(int[] nums) {
        int[] frequency = new int[501];
        int left = 0, answer = 0;
        for (int right = 0; right < nums.length; right++) {
            int value = nums[right];
            while (createsTriple(frequency, value)) frequency[nums[left++]]--;
            frequency[value]++;
            answer = Math.max(answer, right - left + 1);
        }
        return answer;
    }

    private boolean createsTriple(int[] count, int value) {
        // The new element can be the sum or either of its two addends.
        for (int a = 1; a <= value / 2; a++) {
            int b = value - a;
            if (count[a] > 0 && count[b] > (a == b ? 1 : 0)) return true;
        }
        for (int a = 1; a + value < count.length; a++) {
            if (count[a] > 0 && count[a + value] > 0) return true;
        }
        return false;
    }
}