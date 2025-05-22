class Solution {
public:
    int countArrays(vector<int>& original, vector<vector<int>>& bounds) {
        long long lo = bounds[0][0], hi = bounds[0][1];
        for (size_t i = 1; i < original.size(); ++i) {
            long long d = original[i] - original[0];
            lo = max(lo, bounds[i][0] - d);
            hi = min(hi, bounds[i][1] - d);
        }
        return max(0LL, hi - lo + 1);
    }
};