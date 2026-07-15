class Solution {
public:
    int longestSubarray(vector<int>& nums, int k) {
        const int none = nums.size() + 1;
        vector<int> earliest(k, none), adjusted(k, none), seen{0};
        earliest[0] = 0;
        int prefix = 0, longest = 0;
        for (int i = 0; i < nums.size(); ++i) {
            const int correction = ((2 * nums[i]) % k + k) % k;
            // A start already seen can pair with this element as its negation.
            for (int residue : seen) {
                const int wanted = (residue + correction) % k;
                adjusted[wanted] = min(adjusted[wanted], earliest[residue]);
            }
            prefix = ((prefix + nums[i]) % k + k) % k;
            longest = max(longest, i + 1 - min(earliest[prefix], adjusted[prefix]));
            if (earliest[prefix] == none) {
                earliest[prefix] = i + 1;
                seen.push_back(prefix);
            }
        }
        return longest;
    }
};