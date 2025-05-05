class Solution {
public:
    long long maxScore(vector<int>& points, int m) {
        int n = points.size();
        auto ok = [&](long long target) {
            long long moves = 0, extra = 0, skip = 0;
            for (int i = 0; i < n; ++i) {
                long long need = (target + points[i] - 1) / points[i];
                if (extra >= need) {
                    extra = 0;
                    ++skip;
                } else {
                    long long rem = need - extra;
                    moves += skip + 2 * rem - 1;
                    if (moves > m) return false;
                    extra = rem - 1;
                    skip = 0;
                }
            }
            return moves <= m;
        };
        long long lo = 0, hi = 1e15, ans = 0;
        while (lo <= hi) {
            long long mid = lo + (hi - lo) / 2;
            if (ok(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans;
    }
};