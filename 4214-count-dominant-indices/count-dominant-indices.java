class Solution {
    public int dominantIndices(int[] nums) {
        long suffixSum = nums[nums.length - 1];
        int answer = 0;
        for (int i = nums.length - 2; i >= 0; i--) {
            int suffixCount = nums.length - i - 1;
            if ((long) nums[i] * suffixCount > suffixSum) answer++;
            suffixSum += nums[i];
        }
        return answer;
    }
}