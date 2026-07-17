class Solution {
public:
    int maxEqualAdjacentPairs(vector<int>& nums) {
        unordered_map<unsigned long long,int> edges;
        int equal = 0, bestGain = 0;
        for (int i = 1; i < nums.size(); ++i) {
            int a = nums[i - 1], b = nums[i];
            if (a == b) {
                ++equal;
                continue;
            }
            if (a > b) swap(a, b);
            // Merging one pair of value labels makes exactly their shared edges equal.
            auto key = (static_cast<unsigned long long>(a) << 32) | b;
            bestGain = max(bestGain, ++edges[key]);
        }
        return equal + bestGain;
    }
};