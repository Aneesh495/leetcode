class Solution {
public:
    int resilientSubarray(vector<int>& nums, int k) {
        int answer = 1;
        for (int left = 0; left < nums.size();) {
            int remainder = nums[left] % k;
            int right = left + 1;
            while (right < nums.size() && nums[right] % k == remainder) ++right;
            // All deletions give the same remainder only if every element has the same residue.
            int step = k / gcd(k, remainder);
            answer = max(answer, 1 + (right - left - 1) / step * step);
            left = right;
        }
        return answer;
    }
};