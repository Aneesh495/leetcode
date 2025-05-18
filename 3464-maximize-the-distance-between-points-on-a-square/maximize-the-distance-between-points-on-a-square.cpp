class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        int n = points.size();
        vector<long long> t(n);
        long long S = side;
        for (int i = 0; i < n; ++i) {
            long long x = points[i][0], y = points[i][1];
            if (y == 0) t[i] = x;
            else if (x == S) t[i] = S + y;
            else if (y == S) t[i] = 2 * S + (S - x);
            else t[i] = 3 * S + (S - y);
        }
        sort(t.begin(), t.end());
        long long P = 4 * S;
        auto ok = [&](long long d) {
            for (int i = 0; i < n; ++i) {
                long long cur = t[i];
                int idx = i;
                bool good = true;
                for (int step = 1; step < k; ++step) {
                    auto it = lower_bound(t.begin() + idx + 1, t.end(), cur + d);
                    if (it == t.end()) { good = false; break; }
                    idx = it - t.begin();
                    cur = *it;
                }
                if (good && cur - t[i] <= P - d) return true;
            }
            return false;
        };
        long long lo = 1, hi = P / k, ans = 0;
        while (lo <= hi) {
            long long mid = lo + (hi - lo) / 2;
            if (ok(mid)) { ans = mid; lo = mid + 1; }
            else hi = mid - 1;
        }
        return ans;
    }
};