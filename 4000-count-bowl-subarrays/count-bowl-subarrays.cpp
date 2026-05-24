class Solution {
public:
    long long bowlSubarrays(vector<int>& nums) {
        int n = nums.size();
        vector<int> nextGreater(n, n), prevGreater(n, -1), st;
        for (int i = 0; i < n; ++i) {
            while (!st.empty() && nums[st.back()] < nums[i]) {
                nextGreater[st.back()] = i;
                st.pop_back();
            }
            st.push_back(i);
        }
        st.clear();
        for (int i = n - 1; i >= 0; --i) {
            while (!st.empty() && nums[st.back()] < nums[i]) {
                prevGreater[st.back()] = i;
                st.pop_back();
            }
            st.push_back(i);
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (nextGreater[i] < n && nextGreater[i] - i >= 2) ++ans;
            if (prevGreater[i] >= 0 && i - prevGreater[i] >= 2) ++ans;
        }
        return ans;
    }
};