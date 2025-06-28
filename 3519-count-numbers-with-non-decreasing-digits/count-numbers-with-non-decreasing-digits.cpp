class Solution {
public:
    int countNumbers(string l, string r, int b) {
        const int MOD = 1e9 + 7;
        auto toBase = [&](string s, bool dec) {
            if (dec) {
                int i = (int)s.size() - 1;
                while (i >= 0 && s[i] == '0') { s[i] = '9'; --i; }
                if (i >= 0) s[i]--;
            }
            vector<int> digs;
            while (!s.empty() && !(s.size() == 1 && s[0] == '0')) {
                string ns;
                int rem = 0;
                for (char c : s) {
                    int cur = rem * 10 + (c - '0');
                    int q = cur / b;
                    rem = cur % b;
                    if (!ns.empty() || q > 0) ns.push_back('0' + q);
                }
                digs.push_back(rem);
                s = move(ns);
            }
            if (digs.empty()) digs.push_back(0);
            reverse(digs.begin(), digs.end());
            return digs;
        };
        auto solve = [&](const vector<int>& digs) {
            int n = digs.size();
            vector<vector<int>> dp(n + 1, vector<int>(b, 0));
            int memo[350][11][2];
            memset(memo, -1, sizeof(memo));
            auto dfs = [&](auto& self, int pos, int prev, int tight) -> int {
                if (pos == n) return 1;
                if (memo[pos][prev][tight] != -1) return memo[pos][prev][tight];
                int lim = tight ? digs[pos] : b - 1;
                long long res = 0;
                for (int d = prev; d <= lim; ++d) {
                    res = (res + self(self, pos + 1, d, tight && (d == lim))) % MOD;
                }
                return memo[pos][prev][tight] = res;
            };
            return dfs(dfs, 0, 0, 1);
        };
        long long ans = solve(toBase(r, false)) - solve(toBase(l, true));
        return (ans % MOD + MOD) % MOD;
    }
};