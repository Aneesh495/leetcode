class Solution {
    public int countConsistent(int[] nums) {
        int answer = 0;
        for (int left = 0; left < nums.length; left++) {
            int smallest = nums[left];
            int bits = nums[left];
            for (int right = left; right < nums.length; right++) {
                // Extend the current interval by updating its minimum and AND.
                smallest = Math.min(smallest, nums[right]);
                bits &= nums[right];
                if (bits == smallest) answer++;
            }
        }
        return answer;
    }
}