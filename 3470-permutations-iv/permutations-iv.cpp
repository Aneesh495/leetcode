class Solution {
public:
    vector<int> permute(int n, long long k) {
        const long long INF = 2e15;
        vector<long long> fact(n + 1, 1);
        for (int i = 1; i <= n; ++i) fact[i] = min(INF, fact[i - 1] * i);
        auto ways = [&](int o, int e) -> long long {
            if (o < 0 || e < 0) return 0;
            __int128 w = (__int128)fact[o] * fact[e];
            return w > INF ? INF : (long long)w;
        };
        int o = (n + 1) / 2, e = n / 2;
        vector<bool> used(n + 1, false);
        vector<int> ans;
        int last_p = -1;
        for (int pos = 0; pos < n; ++pos) {
            bool found = false;
            for (int x = 1; x <= n; ++x) {
                if (used[x]) continue;
                int p = x & 1;
                if (p == last_p) continue;
                if (pos == 0 && n % 2 == 1 && p == 0) continue;
                int no = o - (p == 1), ne = e - (p == 0);
                if (abs(no - ne) > 1) continue;
                long long w = ways(no, ne);
                if (k <= w) {
                    ans.push_back(x);
                    used[x] = true;
                    o = no; e = ne; last_p = p;
                    found = true;
                    break;
                } else {
                    k -= w;
                }
            }
            if (!found) return {};
        }
        return ans;
    }
};