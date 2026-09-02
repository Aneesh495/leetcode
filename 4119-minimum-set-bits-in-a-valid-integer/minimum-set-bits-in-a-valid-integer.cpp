class Solution {
public:
    int minSetBits(vector<int>& nums, int k) {
        int n = nums.size();
        int cnt[30] = {};
        for (int i = 0; i < k - 1; ++i)
            for (int b = 0; b < 30; ++b) if ((nums[i] >> b) & 1) cnt[b]++;
        vector<int> xs;
        for (int i = k - 1; i < n; ++i) {
            for (int b = 0; b < 30; ++b) if ((nums[i] >> b) & 1) cnt[b]++;
            int x = 0;
            for (int b = 0; b < 30; ++b) if (cnt[b] == k) x |= (1 << b);
            if (x == 0) return -1;
            xs.push_back(x);
            for (int b = 0; b < 30; ++b) if ((nums[i - k + 1] >> b) & 1) cnt[b]--;
        }
        sort(xs.begin(), xs.end());
        xs.erase(unique(xs.begin(), xs.end()), xs.end());
        sort(xs.begin(), xs.end(), [](int a, int b) {
            return __builtin_popcount(a) < __builtin_popcount(b);
        });
        vector<int> f;
        for (int x : xs) {
            bool sup = false;
            for (int y : f) if ((x & y) == y) { sup = true; break; }
            if (!sup) f.push_back(x);
        }
        int best = 31;
        auto dfs = [&](auto& self, vector<int> cur, int bits) -> void {
            while (true) {
                int add = 0;
                for (int x : cur) {
                    if (x == 0) return;
                    if ((x & (x - 1)) == 0) add |= x;
                }
                if (!add) break;
                bits += __builtin_popcount(add);
                if (bits >= best) return;
                vector<int> nxt;
                for (int x : cur) if ((x & add) == 0) nxt.push_back(x);
                cur.swap(nxt);
            }
            if (cur.empty()) { best = min(best, bits); return; }
            if (bits + 1 >= best) return;
            int bestB = -1, bestCov = -1;
            for (int b = 0; b < 30; ++b) {
                int cov = 0;
                for (int x : cur) if ((x >> b) & 1) cov++;
                if (cov > bestCov) { bestCov = cov; bestB = b; }
            }
            if (bestCov == (int)cur.size()) { best = min(best, bits + 1); return; }
            vector<int> withB, withoutB;
            for (int x : cur) {
                if (!((x >> bestB) & 1)) withB.push_back(x);
                int nx = x & ~(1 << bestB);
                if (nx == 0) goto skip_without;
                withoutB.push_back(nx);
            }
            self(self, move(withB), bits + 1);
            self(self, move(withoutB), bits);
            return;
            skip_without:;
            self(self, move(withB), bits + 1);
        };
        dfs(dfs, f, 0);
        return best;
    }
};