class Solution {
public:
    int longestArithmetic(vector<int>& nums) {
        int n = nums.size();
        vector<int> left(n, 1), right(n, 1);
        for (int i = 1; i < n; ++i) {
            left[i] = i >= 2 && nums[i] - nums[i-1] == nums[i-1] - nums[i-2] ? left[i-1] + 1 : 2;
        }
        for (int i = n - 2; i >= 0; --i) {
            right[i] = i + 2 < n && nums[i+1] - nums[i] == nums[i+2] - nums[i+1] ? right[i+1] + 1 : 2;
        }
        int answer = 1;
        for (int i = 0; i < n; ++i) {
            if (i > 0) answer = max(answer, left[i-1] + 1);
            if (i + 1 < n) answer = max(answer, right[i+1] + 1);
            if (i == 0 || i + 1 == n) continue;
            int difference = nums[i+1] - nums[i-1];
            if (difference % 2 != 0) continue;
            int step = difference / 2;
            // Changing the middle element can join runs only when both have the forced step.
            int before = i >= 2 && nums[i-1] - nums[i-2] == step ? left[i-1] : 1;
            int after = i + 2 < n && nums[i+2] - nums[i+1] == step ? right[i+1] : 1;
            answer = max(answer, before + 1 + after);
        }
        return answer;
    }
};