class Solution {
public:
    long long maxSubarrays(int n, vector<vector<int>>& conflictingPairs) {
        vector<vector<int>> lefts(n + 1);
        for (auto& p : conflictingPairs) {
            int a = min(p[0], p[1]), b = max(p[0], p[1]);
            lefts[b].push_back(a);
        }
        long long base = 0;
        int b1 = 0, b2 = 0;
        vector<long long> gain(n + 1, 0);
        for (int r = 1; r <= n; ++r) {
            for (int l : lefts[r]) {
                if (l > b1) { b2 = b1; b1 = l; }
                else if (l > b2) b2 = l;
            }
            base += r - b1;
            gain[b1] += b1 - b2;
        }
        return base + *max_element(gain.begin(), gain.end());
    }
};