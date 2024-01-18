class Solution {
    public long[] findPrefixScore(int[] nums) {
        long[] answer = new long[nums.length];
        long prefixMax = 0;
        long score = 0;
        for (int i = 0; i < nums.length; i++) {
            prefixMax = Math.max(prefixMax, nums[i]);
            score += nums[i] + prefixMax;
            answer[i] = score;
        }
        return answer;
    }
}